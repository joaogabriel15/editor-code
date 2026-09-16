"""Check that all inspected structural upstream entries have owners in the plan."""
import argparse
import json
import pathlib
import urllib.request

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--tree", type=pathlib.Path, help="Previously downloaded GitHub recursive tree JSON")
    args = parser.parse_args()
    root = pathlib.Path(__file__).resolve().parents[1]
    plan = json.loads((root / "docs/planning/parity-plan.json").read_text(encoding="utf-8"))
    if args.tree:
        tree = json.loads(args.tree.read_text(encoding="utf-8"))
    else:
        url = "https://api.github.com/repos/microsoft/vscode/git/trees/" + plan["reference"]["sha"] + "?recursive=1"
        request = urllib.request.Request(url, headers={"User-Agent": "Editor-Code-planning-audit"})
        with urllib.request.urlopen(request, timeout=60) as response:
            tree = json.load(response)
    assert not tree.get("truncated"), "Incomplete upstream tree"
    groups = {
        "workbench": "src/vs/workbench/contrib/",
        "editor": "src/vs/editor/contrib/",
        "sessions": "src/vs/sessions/contrib/",
        "platform": "src/vs/platform/",
        "service": "src/vs/workbench/services/",
    }
    for kind, prefix in groups.items():
        expected = {x["path"][len(prefix):] for x in tree["tree"]
                    if x["type"] == "tree" and x["path"].startswith(prefix)
                    and "/" not in x["path"][len(prefix):]}
        observed = {x["key"] for x in plan["inventory"] if x["kind"] == kind}
        assert expected == observed, f"{kind}: missing={expected-observed}, stale={observed-expected}"
    expected = {x["path"].split("/")[1] for x in tree["tree"]
                if x["path"].startswith("extensions/") and x["path"].endswith("/package.json")
                and len(x["path"].split("/")) == 3}
    observed = {x["key"] for x in plan["inventory"] if x["kind"] == "builtin"}
    assert expected == observed, f"Builtin manifests: missing={expected-observed}, stale={observed-expected}"
    expected = {x["path"].split("vscode.proposed.")[1][:-5] for x in tree["tree"]
                if x["path"].startswith("src/vscode-dts/vscode.proposed.") and x["path"].endswith(".d.ts")}
    observed = {x["key"] for x in plan["inventory"] if x["kind"] == "proposed-api"}
    assert expected == observed, f"Proposals: missing={expected-observed}, stale={observed-expected}"
    print("All seven structural source groups match the inspected upstream tree.")
    print("This check does not validate API semantics or product behavior.")

if __name__ == "__main__":
    main()
