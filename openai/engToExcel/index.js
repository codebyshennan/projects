import { Configuration, OpenAIApi } from 'openai'

const configuration = new Configuration({
  apiKey: process.env.OPENAI_API_KEY,
})
const openai = new OpenAIApi(configuration)

const response = await openai.createCompletion({
  model: 'text-davinci-002',
  prompt: 'Create a javascript Stripe client connection',
  temperature: 0.5,
  max_tokens: 100,
  top_p: 1.0,
  frequency_penalty: 0.0,
  presence_penalty: 0.0,
})

console.log(JSON.stringify(response.data))

// const solution = {
//   id: 'cmpl-69WXWwPyHLIj6WK2yEEsxjoM4PtZv',
//   object: 'text_completion',
//   created: 1667728054,
//   model: 'text-davinci-002',
//   choices: [
//     {
//       text: '\n\n=SUMIF(B:B,"marketing",A:A)',
//       index: 0,
//       logprobs: null,
//       finish_reason: 'stop',
//     },
//   ],
//   usage: { prompt_tokens: 30, completion_tokens: 18, total_tokens: 48 },
// }
