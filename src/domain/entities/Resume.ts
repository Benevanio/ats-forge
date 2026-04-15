export interface RawExperience {
  empresa: string;
  cargo: string;
  periodo: string;
  stack: string;
  atividades: string[];
  resultados?: string[];
}

export interface Resume {
  nome: string;
  email: string;
  telefone: string;
  linkedin: string;
  github: string;
  portfolio: string;
  experiencias: RawExperience[];
  formacao: string[];
  idiomas: string[];
}
