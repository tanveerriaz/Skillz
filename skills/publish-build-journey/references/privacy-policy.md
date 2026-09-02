# Publication privacy policy

Apply this policy before preparing any public-ready copy or media.

## Never publish

- API keys, tokens, passwords, cookies, authorization headers, private keys, recovery codes, or secret values.
- `.env` content, credential files, keychain output, browser/session storage, shell history, or secret-manager output.
- Absolute local paths, local usernames, hostnames, device names, private IP addresses, internal domains, or infrastructure identifiers.
- Exact home, office, hotel, travel, or real-time location. Remove GPS and EXIF location metadata.
- Personal email addresses, phone numbers, identification numbers, account/card numbers, or financial records unless the user separately and explicitly approves a specific public contact field.
- Customer, client, employee, colleague, family, or attendee data that is not already a necessary part of an approved public source.
- Employer-confidential systems, screenshots, prompts, architecture, incidents, code, data, strategy, controls, or agent implementation details.
- Private repository names, contents, URLs, branch names, issue text, or contribution claims derived from private work.
- Agent memory, private personas, budgets, internal instructions, approval policies, or orchestration configuration.

## Public-safe defaults

- Publish names, biographies, locations, employment history, and contact links only when the user explicitly approves those exact fields for the named destination.
- Use verified public repositories, project URLs, credentials, and user-approved event photographs.
- Describe personal experiments at the principle level unless implementation details already have an approved public source.
- Describe enterprise exploration as perspective, never as proof of an employer deployment.
- Label fictional interfaces and demonstrations as mock or sample data.

## Combination risk

Individually harmless details can reveal sensitive information when combined. Review dates, photos, venue names, travel context, schedules, device information, and employer references together.

If a photo establishes a precise location, do not pair it with real-time language. Prefer retrospective month/year context after the event.

## Automated scan handling

- Treat every high-severity finding as blocking.
- Never print the matched secret. Report category, path, and line only.
- Treat medium findings as requiring human review.
- A zero-finding scan does not authorize publication.

## Final semantic checklist

- Could this reveal where the user is right now?
- Could this expose how to access a system or account?
- Could this identify private work, people, or organizational structure?
- Is every performance, model, and “latest” claim dated and sourced?
- Are demos, sample data, and generated images unmistakably labelled?
- Is the public value preserved after removing implementation detail?
- Has the user approved this exact version and destination?
