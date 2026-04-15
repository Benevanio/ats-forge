export interface IKeywordExtractor {
  extract(source: string | null): string[];
}
