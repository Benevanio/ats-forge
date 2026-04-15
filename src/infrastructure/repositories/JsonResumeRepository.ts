import fs from 'fs';
import path from 'path';
import { Resume } from '../../domain/entities/Resume';
import { IResumeRepository } from '../../domain/interfaces/IResumeRepository';

const REQUIRED_FIELDS: ReadonlyArray<keyof Resume> = [
  'nome', 'email', 'telefone', 'linkedin',
  'github', 'portfolio', 'experiencias', 'formacao',
];

export class JsonResumeRepository implements IResumeRepository {
  constructor(private readonly filePath: string) {}

  load(): Resume {
    if (!fs.existsSync(this.filePath)) {
      throw new Error(
        `Arquivo de currículo não encontrado: ${this.filePath}\n` +
        `Execute:  cp resume.example.json resume.json  e preencha com seus dados.`,
      );
    }

    let raw: unknown;
    try {
      raw = JSON.parse(fs.readFileSync(this.filePath, 'utf-8'));
    } catch (err) {
      throw new Error(
        `Falha ao parsear ${path.basename(this.filePath)}: ${(err as Error).message}`,
      );
    }

    this.validate(raw as Record<string, unknown>);
    return raw as Resume;
  }

  private validate(data: Record<string, unknown>): void {
    for (const field of REQUIRED_FIELDS) {
      if (!data[field]) {
        throw new Error(`Campo obrigatório ausente no resume.json: "${field}"`);
      }
    }

    if (!Array.isArray(data['experiencias']) || (data['experiencias'] as unknown[]).length === 0) {
      throw new Error('resume.json deve conter ao menos uma experiência.');
    }

    for (const [i, exp] of (data['experiencias'] as Record<string, unknown>[]).entries()) {
      for (const key of ['empresa', 'cargo', 'periodo', 'stack', 'atividades']) {
        if (!exp[key]) {
          throw new Error(`Experiência [${i}] está faltando o campo: "${key}"`);
        }
      }
    }
  }
}
