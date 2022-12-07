import { AocClient } from "advent-of-code-client";
import dotenv from "dotenv";

dotenv.config();

const date = new Date();

const getClient = (year?: number, day?: number) =>
  new AocClient({
    year: year == undefined ? date.getFullYear() : year,
    day:
      day == undefined
        ? date.getHours() > 20
          ? date.getDate() + 1
          : date.getDate()
        : day,
    token: process.env.SESSION_COOKIE ?? "",
  });

export { getClient };
