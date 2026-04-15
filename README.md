# ATS CV Generator

> **Template** — Generate ATS-friendly resumes in DOCX and Markdown from a single JSON file.  
> Built with **TypeScript** and **Clean Architecture**.

## Features

- Generates `.docx` and `.md` resumes tailored to multiple job focuses  
- Extracts keywords from a job description and injects them into the resume  
- All personal data lives in a single `resume.json` (gitignored — never committed)  
- All focus configuration lives in `config/` JSON files — no TypeScript changes needed  
- Clean Architecture: Domain → Application → Infrastructure → Presentation  

---

## Quick Start

```bash
# 1. Clone / use this template
git clone https://github.com/your-user/ats-cv-generator.git
cd ats-cv-generator

# 2. Install dependencies
npm install

# 3. Create your personal resume file
cp resume.example.json resume.json
# ✏️  Edit resume.json with your real data

# 4. Generate all resumes (DOCX)
npm run generate -- --all

# 5. Find the results in ./output/
```

---

## Customization

### 1. Your personal data → `resume.json`

Copy `resume.example.json` to `resume.json` and fill in every field.  
`resume.json` is gitignored — your personal data never leaves your machine.

### 2. Job focuses → `config/focuses.json`

Each key is a focus identifier. You can add, rename, or remove focuses.

```jsonc
{
  "node_react": {
    "filename": "Resume_Node_React.docx",
    "title": "Node.js Full Stack Engineer"
  }
}
```

### 3. Professional profiles → `config/profiles.json`

One paragraph per focus. Written in first or third person — your choice.

```jsonc
{
  "node_react": "Software Engineer specialized in..."
}
```

### 4. Skills → `config/skills.json`

Grouped by category. Categories appear in the order defined here.

```jsonc
{
  "node_react": {
    "Languages": ["TypeScript", "JavaScript"],
    "Backend":   ["Node.js", "Express.js"]
  }
}
```

### 5. Impact rules → `config/impact-rules.json`

Maps company names (matching exactly what's in `resume.json`) to keyword-based impact statements.  
When an activity matches any keyword in a rule, the result is appended to that activity.

```jsonc
{
  "Acme Corp": [
    {
      "keywords": ["api", "rest"],
      "result": "30% reduction in service response time"
    }
  ]
}
```

---

## CLI Usage

```bash
# All focuses (DOCX)
npm run generate -- --all

# Single focus
npm run generate -- --focus=node_react

# Tailored with a job description
npm run generate -- --focus=node_react --job=job-description.txt

# All focuses in Markdown
npm run generate -- --all --markdown

# With a job description + all focuses
npm run generate -- --all --job=job-description.txt
```

**Available flags:**

| Flag | Description |
|------|-------------|
| `--all` | Generate all configured focuses |
| `--focus=<id>` | Generate a single focus |
| `--job=<file>` | Path to a job description `.txt` file for keyword extraction |
| `--markdown` | Output `.md` instead of `.docx` |

---

## Project Structure

```
ats-cv-generator/
├── src/
│   ├── domain/                     # Business rules (no external dependencies)
│   │   ├── entities/
│   │   │   ├── Resume.ts           # Resume + RawExperience types
│   │   │   └── EnrichedExperience.ts
│   │   ├── interfaces/
│   │   │   ├── IResumeRepository.ts
│   │   │   ├── IResumeRenderer.ts
│   │   │   ├── IKeywordExtractor.ts
│   │   │   ├── IOutputRepository.ts
│   │   │   └── IConfigRepository.ts
│   │   └── services/
│   │       └── ImpactEnricher.ts   # Domain service: enriches activities with metrics
│   ├── application/                # Use cases (orchestration only)
│   │   ├── dtos/
│   │   │   └── GenerateResumeInput.ts
│   │   └── use-cases/
│   │       └── GenerateResumeUseCase.ts
│   ├── infrastructure/             # External adapters
│   │   ├── config/
│   │   │   └── ConfigLoader.ts     # Reads config/*.json
│   │   ├── keyword-extractors/
│   │   │   └── FileKeywordExtractor.ts
│   │   ├── renderers/
│   │   │   ├── DocxResumeRenderer.ts
│   │   │   └── MarkdownResumeRenderer.ts
│   │   └── repositories/
│   │       ├── JsonResumeRepository.ts  # Reads resume.json
│   │       └── FileOutputRepository.ts # Writes to output/
│   ├── presentation/
│   │   └── cli/
│   │       ├── ArgParser.ts        # Parses CLI args
│   │       └── CliController.ts    # Composition root + wires dependencies
│   └── main.ts                     # Entry point
├── config/                         # ✏️  Customize these JSON files
│   ├── focuses.json                # Focus IDs, titles, output filenames
│   ├── profiles.json               # Professional summaries per focus
│   ├── skills.json                 # Skills grouped by category per focus
│   └── impact-rules.json          # Keyword → metric rules per company
├── resume.example.json             # Template — copy to resume.json
├── resume.json                     # ← Your data (gitignored)
├── output/                         # Generated resumes (gitignored)
├── tsconfig.json
└── package.json
```

---

## Architecture

```
         CLI args
              │
    ┌─────────▼──────────┐
    │  Presentation/CLI  │  ArgParser + CliController
    └─────────┬──────────┘
              │ GenerateResumeInput
    ┌─────────▼──────────┐
    │   Application      │  GenerateResumeUseCase
    └──┬───┬───┬───┬─────┘
       │   │   │   │        (all via interfaces)
       │   │   │   └──► IOutputRepository
       │   │   └──────► IKeywordExtractor
       │   └──────────► IResumeRenderer
       └──────────────► IResumeRepository + IConfigRepository
              │
    ┌─────────▼──────────┐
    │   Infrastructure   │  Concrete implementations
    └────────────────────┘
```

The domain layer has **zero external dependencies** — no `fs`, no `docx`, no `path`.

---

## Building (compiled output)

```bash
npm run build          # compiles to dist/
npm run generate:compiled -- --all
```

---

## License

MIT
