# Website repository instructions

This is the public CarnaticTranslate prelaunch website. Read the assigned issue and inspect fresh remote refs plus staged, unstaged and untracked changes before acting. Preserve existing files and staging; use an isolated checkout when appropriate. Do not stash, reset, clean, force-push or broadly stage existing work.

## Validation

- Run `python3 scripts/check-site.py` and `git diff --check`. The script checks HTML nesting, IDs, navigation, local references, accessibility targets and image/video basics without calling external services.
- Check the case-sensitive `/CarnaticTranslate/` project path and relevant navigation/anchors. Review desktop/mobile rendering when visible changes justify it; reuse unchanged accepted evidence without claiming a fresh browser pass.
- Preserve PR #3 as its separate release-draft review. This prelaunch publication candidate uses the accepted homepage/assets and beta policies at privacy.html/terms.html, without draft/not-yet-effective labels at app-linked URLs. Do not invent effective dates; record publication-date and material-change notice approval in the PR before publication. Keep Coming soon and the approved policy-change notice provisions intact. Do not infer provider activation, implemented age/guardian safeguards, deletion availability or account retention settings from policy text.
- Reference the issue, record meaningful checks and limits, link the resulting PR, and set accurate issue/Project status. Identify publication follow-up explicitly.

## Public-safe scope

Commit only necessary public site files/assets and checks. Never commit private operational handoffs, review screenshots, credentials, local state or generated output. `.release-review/` stays excluded; detailed internal evidence belongs in the owner's private coordination records. Public issues/PRs must contain sanitized outcomes, without private repository links or operational details.

## Publishing boundary

The verified Pages configuration publishes **main / repository root**. Pushing to or merging into `main` can publish immediately. A preservation PR is for review only: **do not merge or publish until the owner separately authorizes publication** and the release facts/dates are approved.

Before pushing another branch or opening a PR, verify current Pages settings and workflow/webhook triggers; do not assume old settings still apply. Do not change Pages configuration, invoke publishing workflows, add deployment automation or treat code review as publication approval. Preserve the existing site candidate unless the assigned task explicitly authorizes changes; no redesign, new legal-policy decision, provider call, purchase or scan is implied.
