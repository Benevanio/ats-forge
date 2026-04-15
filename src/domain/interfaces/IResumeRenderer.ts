import { EnrichedExperience } from '../entities/EnrichedExperience';

export interface RenderContact {
  nome: string;
  email: string;
  telefone: string;
  linkedin: string;
  github: string;
  portfolio: string;
  formacao: string[];
  idiomas: string[];
}

export interface RenderPayload {
  contact: RenderContact;
  focus: string;
  title: string;
  profile: string;
  skills: Record<string, string[]>;
  experiencias: EnrichedExperience[];
  extraKeywords: string[];
}

export interface IResumeRenderer {
  readonly extension: string;
  render(payload: RenderPayload): Promise<Buffer | string>;
}
