import fs from 'fs';
import path from 'path';
import { IConfigRepository, ResumeConfig } from '../../domain/interfaces/IConfigRepository';

export class ConfigLoader implements IConfigRepository {
  private cached: ResumeConfig | null = null;

  constructor(private readonly configDir: string) {}

  load(): ResumeConfig {
    if (this.cached) return this.cached;

    this.cached = {
      focuses: this.readJson('focuses.json'),
      profiles: this.readJson('profiles.json'),
      skills: this.readJson('skills.json'),
      impactRules: this.readJson('impact-rules.json'),
    };

    return this.cached;
  }

  private readJson<T>(filename: string): T {
    const filePath = path.join(this.configDir, filename);
    if (!fs.existsSync(filePath)) {
      throw new Error(`Arquivo de configuração não encontrado: ${filePath}`);
    }
    try {
      return JSON.parse(fs.readFileSync(filePath, 'utf-8')) as T;
    } catch (err) {
      throw new Error(`Falha ao parsear ${filename}: ${(err as Error).message}`);
    }
  }
}
