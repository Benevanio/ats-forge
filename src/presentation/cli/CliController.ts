import path from 'path';
import { GenerateResumeUseCase } from '../../application/use-cases/GenerateResumeUseCase';
import { ConfigLoader } from '../../infrastructure/config/ConfigLoader';
import { FileKeywordExtractor } from '../../infrastructure/keyword-extractors/FileKeywordExtractor';
import { DocxResumeRenderer } from '../../infrastructure/renderers/DocxResumeRenderer';
import { MarkdownResumeRenderer } from '../../infrastructure/renderers/MarkdownResumeRenderer';
import { FileOutputRepository } from '../../infrastructure/repositories/FileOutputRepository';
import { JsonResumeRepository } from '../../infrastructure/repositories/JsonResumeRepository';
import { parseArgs, printHelp } from './ArgParser';

// Project root is three levels up from src/presentation/cli/
const ROOT = path.resolve(__dirname, '..', '..', '..');

export async function run(argv: string[]): Promise<void> {
  const args = parseArgs(argv);
  const configRepo = new ConfigLoader(path.join(ROOT, 'config'));

  if (!args.all && !args.focus) {
    const config = configRepo.load();
    printHelp(Object.keys(config.focuses));
    process.exit(1);
  }

  const config = configRepo.load();

  if (args.focus && !config.focuses[args.focus]) {
    console.error(`[erro] Foco inválido: "${args.focus}"`);
    console.error(`Focos válidos: ${Object.keys(config.focuses).join(', ')}`);
    process.exit(1);
  }

  const renderer =
    args.format === 'markdown' ? new MarkdownResumeRenderer() : new DocxResumeRenderer();

  const useCase = new GenerateResumeUseCase(
    new JsonResumeRepository(path.join(ROOT, 'resume.json')),
    configRepo,
    renderer,
    new FileKeywordExtractor(),
    new FileOutputRepository(path.join(ROOT, 'output')),
  );

  await useCase.execute({
    focus: args.focus,
    all: args.all,
    jobDescriptionPath: args.jobDescriptionPath
      ? path.resolve(args.jobDescriptionPath)
      : null,
  });
}
