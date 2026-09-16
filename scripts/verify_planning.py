"""Validate planning traceability; this does not validate implemented product features."""
import argparse
import collections
import json
import pathlib
import re

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--require-published", action="store_true")
    args = parser.parse_args()
    root = pathlib.Path(__file__).resolve().parents[1]
    plan = json.loads((root / "docs/planning/parity-plan.json").read_text(encoding="utf-8"))
    tasks = plan["tasks"]
    ids = {t["id"] for t in tasks}
    assert len(ids) == len(tasks), "Duplicate task IDs"
    assert ids == set(range(1, max(ids) + 1)), "Missing task ID"
    by_id = {t["id"]: t for t in tasks}
    visiting, visited = set(), set()

    def visit(task_id):
        assert task_id not in visiting, f"Dependency cycle at EC-{task_id:03}"
        if task_id in visited:
            return
        visiting.add(task_id)
        for dependency in by_id[task_id]["deps"]:
            assert dependency in ids, f"Unknown dependency: {dependency}"
            visit(dependency)
        visiting.remove(task_id)
        visited.add(task_id)

    for task in tasks:
        visit(task["id"])
        assert task["status"] in {"planejado", "implementado", "verificado", "parcial", "bloqueado"}
        if task["id"] > 30:
            assert len(task["accept"]) >= 3 and task["sources"], "Missing criteria/source"
        if args.require_published:
            assert isinstance(task["issue"], int) and task["issue"] > 0, "Unpublished issue"
    assigned = [t["issue"] for t in tasks if t.get("issue")]
    assert len(set(assigned)) == len(assigned), "Duplicate GitHub issue assignment"
    unique = set()
    for row in plan["inventory"]:
        key = (row["kind"], row["key"])
        assert key not in unique, f"Duplicate inventory row: {key}"
        unique.add(key)
        assert row["owners"] and all(n in ids for n in row["owners"]), f"Unowned entry: {key}"
        assert plan["reference"]["sha"] in row["source"], "Unpinned source"
        assert row["status"] in {"planejado", "implementado", "verificado", "parcial", "bloqueado"}
        if row["status"] == "verificado":
            assert row.get("evidence"), "Verified entry requires evidence"
    assert dict(collections.Counter(r["kind"] for r in plan["inventory"])) == plan["counts"]
    # Local Markdown targets should resolve; external URLs are not fetched by this offline check.
    for doc in [root / "README.md", *list((root / "docs").rglob("*.md"))]:
        for dest in re.findall(r"\]\(([^)]+)\)", doc.read_text(encoding="utf-8")):
            if "://" in dest or dest.startswith("#"):
                continue
            path = dest.split("#", 1)[0]
            if path:
                assert (doc.parent / path).exists(), f"Broken local link: {doc}: {dest}"
    print(f"Planning valid: {len(tasks)} tasks; {len(plan['inventory'])} owned inventory entries; acyclic dependencies.")
    print("This is structural coverage, not feature implementation or verified VS Code parity.")

if __name__ == "__main__":
    main()
