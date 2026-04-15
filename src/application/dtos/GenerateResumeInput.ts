export interface GenerateResumeInput {
  /** Specific focus to generate, or null when `all` is true. */
  focus: string | null;
  /** Generate all configured focuses. */
  all: boolean;
  /** Absolute path to a job description file for keyword extraction. */
  jobDescriptionPath: string | null;
}
