import fs from 'fs';
import { IKeywordExtractor } from '../../domain/interfaces/IKeywordExtractor';

const STOP_WORDS = new Set([
  'e', 'de', 'da', 'do', 'em', 'com', 'para', 'por', 'os', 'as',
  'um', 'uma', 'o', 'a', 'que', 'se', 'na', 'no', 'ao', 'aos',
  'das', 'dos', 'nos', 'nas', 'sua', 'seu', 'ser', 'foi', 'são',
  'the', 'and', 'or', 'in', 'of', 'to', 'for', 'with', 'is',
  'are', 'you', 'we', 'our', 'be', 'at', 'on', 'an', 'us', 'it',
  'this', 'that', 'will', 'have', 'has', 'not',
]);

export class FileKeywordExtractor implements IKeywordExtractor {
  extract(filePath: string | null): string[] {
    if (!filePath) return [];

    if (!fs.existsSync(filePath)) {
      console.warn(`[aviso] Arquivo de descrição da vaga não encontrado: ${filePath}`);
      return [];
    }

    return this.extractFromText(fs.readFileSync(filePath, 'utf-8'));
  }

  private extractFromText(text: string): string[] {
    const seen = new Set<string>();
    return text
      .toLowerCase()
      .split(/[\s,.\-/()\[\]{}:;|+&'"!\n\r\t]+/)
      .map((w) => w.trim())
      .filter(
        (w) =>
          w.length > 2 &&
          !STOP_WORDS.has(w) &&
          /[a-záéíóúàãõêâçA-Z0-9]/.test(w),
      )
      .filter((w) => {
        if (seen.has(w)) return false;
        seen.add(w);
        return true;
      });
  }
}
