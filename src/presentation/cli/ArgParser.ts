export interface CliArgs {
  focus: string | null;
  all: boolean;
  jobDescriptionPath: string | null;
  format: 'docx' | 'markdown';
}

export function parseArgs(argv: string[]): CliArgs {
  const args: CliArgs = {
    focus: null,
    all: false,
    jobDescriptionPath: null,
    format: 'docx',
  };

  for (const arg of argv.slice(2)) {
    if (arg === '--all') {
      args.all = true;
    } else if (arg.startsWith('--focus=')) {
      args.focus = arg.slice('--focus='.length).trim();
    } else if (arg.startsWith('--job=')) {
      args.jobDescriptionPath = arg.slice('--job='.length).trim();
    } else if (arg === '--markdown') {
      args.format = 'markdown';
    } else {
      console.warn(`[aviso] Argumento desconhecido ignorado: ${arg}`);
    }
  }

  return args;
}

export function printHelp(validFocuses: string[]): void {
  console.log(`
Uso:
  npm run generate -- --all                          Gera todos os currículos (DOCX)
  npm run generate -- --focus=<foco>                 Gera apenas o foco indicado
  npm run generate -- --focus=<foco> --job=<arquivo> Gera com palavras-chave da vaga
  npm run generate -- --all --job=<arquivo>          Todos + palavras-chave da vaga
  npm run generate -- --all --markdown               Gera em Markdown ao invés de DOCX

Focos disponíveis:
  ${validFocuses.join('\n  ')}
`);
}
