import { Resume } from '../entities/Resume';

export interface IResumeRepository {
  load(): Resume;
}
