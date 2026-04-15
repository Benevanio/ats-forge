import fs from 'fs';
import path from 'path';
import { IOutputRepository } from '../../domain/interfaces/IOutputRepository';

export class FileOutputRepository implements IOutputRepository {
  constructor(private readonly outputDir: string) {}

  ensureDir(): void {
    if (!fs.existsSync(this.outputDir)) {
      fs.mkdirSync(this.outputDir, { recursive: true });
    }
  }

  save(data: Buffer | string, filename: string): void {
    fs.writeFileSync(path.join(this.outputDir, filename), data);
  }
}
