# Create a sourced newspaper

Turn supplied HTML, Excel, email, Teams and transcripts into a source-attributed newspaper. The organization-neutral template uses blue and green, a serif masthead, ruled columns, responsive layouts and restrained motion. It is not an official corporate brand asset.

The renderer uses Python 3.9+ and the standard library. It makes no network calls and installs no dependencies. Source collection belongs to your authorized agent host and its connected tools.

## GitHub Copilot

Copy this complete directory to `.github/skills/create-sourced-newspaper/` in your working repository. Keep `SKILL.md`, `assets`, `references` and `scripts` together. Ask Copilot to use `create-sourced-newspaper` and supply the approved input files or source locations.

- [GitHub cloud agent skill setup](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills)
- [VS Code agent skills](https://code.visualstudio.com/docs/agent-customization/agent-skills)

Installing a skill does not grant Microsoft 365 access. Do not commit private source files, edition JSON or internal rendered newspapers to public repositories.

## Microsoft 365 Copilot

Where your tenant exposes Skills, package the **contents** of this directory as a ZIP, with `SKILL.md` at the ZIP root. Do not add a containing `create-sourced-newspaper/` folder. Exclude generated editions and Python cache files.

Upload the ZIP using the supported skill-import flow in your Microsoft 365 Copilot surface. Configure source knowledge, tools and permissions separately. Features, Python execution and file output depend on your tenant, license, host and admin policy. If script execution is unavailable, use the editorial instructions and render the normalized JSON in an authorized Python host.

- [Agent Builder skills](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agent-builder-add-skills)
- [Copilot Cowork customization](https://learn.microsoft.com/en-us/copilot/cowork/cowork-customize)

## Try the fictional demo

From this directory:

```sh
python3 scripts/render_newspaper.py --input assets/example-edition.json --output /tmp/newspaper-demo.html
python3 scripts/test_renderer.py
```

Open the HTML in a modern browser. It contains all content locally, including source notes. The bundled HTML, workbook, email, chat and transcript fixtures are explicitly fictional. They are examples, not current reporting.

## Copy-and-use prompt

> Use create-sourced-newspaper to create a polished newspaper for [audience], covering [topic] for [date range and timezone]. Read only these supplied or authorized sources: [files, workbook sheets, email threads, Teams conversations, transcripts and public topics]. Reconcile conflicting figures. Distinguish approved decisions, proposals, attributed statements and analysis. Cite each factual paragraph and metric with exact source locators. Use the responsive blue-and-green template and its accessible motion, search, filters, source details and print styles. Deliver a standalone HTML file and a coverage/limitations note. Do not invent facts, source links or access. Do not distribute the result beyond this conversation unless I separately ask.

For real reporting, read [the data contract](references/data-contract.md), replace the synthetic material and set `sample` to `false` only after the evidence review. The renderer rejects demo-classified sources in a real edition. It checks structure and references; it cannot determine factual truth or permission.

## Theme and interaction

An optional `theme` object in the edition JSON accepts allowlisted six-digit hex colors. See the data contract for keys. Recheck contrast after changing the palette. Do not imply a brand endorsement or add a logo without authorization.

Search and section buttons filter stories. Numbered citations open source details. Motion respects the system's reduced-motion preference and has a manual control. With JavaScript disabled, all reporting and source details remain readable. Browser printing restores all stories.

JavaScript generally does not work in email bodies. Use an authorized HTML attachment or hosted page. Corporate policy may block HTML attachments. Anyone receiving the file can read its embedded source text, even if a linked original requires separate access.

## Verification and limits

The renderer has 15 automated tests for validation, computed totals, safe links, escaped text, attribution and theme input. The fixture workbook records 84 completed checks out of 100, with matching formulas and cached values.

Responsive, keyboard, modal, motion and print behavior are implemented, but browser/device testing was not completed in the build environment. Follow [the design and QA checklist](references/design-and-qa.md) in your actual browser and tenant. This is not a device certification or full accessibility audit.

The skill does not create persistent access, store credentials, schedule editions, buy sources or publish automatically.
