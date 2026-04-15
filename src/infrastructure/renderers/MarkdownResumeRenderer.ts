import { IResumeRenderer, RenderPayload } from '../../domain/interfaces/IResumeRenderer';

export class MarkdownResumeRenderer implements IResumeRenderer {
  readonly extension = '.md';

  async render(payload: RenderPayload): Promise<string> {
    const { contact, title, profile, skills, experiencias, extraKeywords } = payload;

    const keywordsSection =
      extraKeywords.length > 0
        ? `\n> **Palavras-chave da vaga:** ${extraKeywords.slice(0, 12).join(', ')}\n`
        : '';

    const experiencesSection = experiencias
      .map((exp) => {
        const activities = exp.atividades.map((a) => `- ${a}`).join('\n');
        const results =
          exp.resultados.length > 0
            ? `\n**Resultados Relevantes:**\n${exp.resultados.map((r) => `- ${r}`).join('\n')}`
            : '';
        return [
          `**${exp.empresa} – ${exp.cargo}**`,
          `${exp.periodo} | Stack: ${exp.stack}`,
          '',
          activities,
          results,
        ]
          .join('\n')
          .trimEnd();
      })
      .join('\n\n---\n\n');

    const skillsSection = Object.entries(skills)
      .map(([cat, items]) => `**${cat}:** ${items.join(', ')}`)
      .join('\n');

    return `# ${contact.nome}
## ${title}

${contact.email} | ${contact.telefone}
${contact.linkedin} | ${contact.github}
Portfólio: ${contact.portfolio}
${keywordsSection}
---

## RESUMO PROFISSIONAL

${profile}

---

## EXPERIÊNCIA PROFISSIONAL

${experiencesSection}

---

## FORMAÇÃO ACADÊMICA

${contact.formacao.map((f) => `- ${f}`).join('\n')}

---

## HABILIDADES TÉCNICAS

${skillsSection}

---

## IDIOMAS

${contact.idiomas.map((i) => `- ${i}`).join('\n')}
`;
  }
}
