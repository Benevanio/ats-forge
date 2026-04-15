import { ImpactRule } from '../interfaces/IConfigRepository';

/**
 * Domain service: enriches an activity description with a measurable
 * result when its text matches a configured impact rule.
 */
export class ImpactEnricher {
  constructor(private readonly rules: Record<string, ImpactRule[]>) {}

  enrich(activity: string, company: string, usedResults: Set<string>): string {
    const companyRules = this.rules[company] ?? [];
    const lower = activity.toLowerCase();

    for (const rule of companyRules) {
      if (usedResults.has(rule.result)) continue;
      if (rule.keywords.some((kw) => lower.includes(kw))) {
        usedResults.add(rule.result);
        return `${activity}, contribuindo para: ${rule.result}`;
      }
    }

    return activity;
  }
}
