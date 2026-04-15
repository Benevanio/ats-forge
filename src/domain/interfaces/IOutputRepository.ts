export interface IOutputRepository {
  ensureDir(): void;
  save(data: Buffer | string, filename: string): void;
}
