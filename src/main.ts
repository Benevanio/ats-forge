import { run } from './presentation/cli/CliController';

run(process.argv).catch((err: Error) => {
  console.error(`[erro] ${err.message}`);
  process.exit(1);
});
