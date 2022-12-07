import { Err, Ok, Result } from "ts-results";

const safeParseInt = (s: string): Result<number, string> => {
  let result: number = parseInt(s);
  if (isNaN(result)) {
    return Err(`{s} could not be parsed as number`);
  }
  return Ok(result);
};

export { safeParseInt };
