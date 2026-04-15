export interface FocusConfig {
  filename: string;
  title: string;
}

export interface ImpactRule {
  keywords: string[];
  result: string;
}

export interface ResumeConfig {
  focuses: Record<string, FocusConfig>;
  profiles: Record<string, string>;
  skills: Record<string, Record<string, string[]>>;
  impactRules: Record<string, ImpactRule[]>;
}

export interface IConfigRepository {
  load(): ResumeConfig;
}
