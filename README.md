<p align="center">
  <img src="./OIG.jpg" alt="Robot reading the newspaper"/>
</p>
<h1 align="center">
  Azure Open AI performance test code
  <br>
</h1>

<h4 align="center">Python code that will help you test the performance I.e. call latency of various <a href="urlhttps://learn.microsoft.com/en-us/azure/ai-services/openai/overview">Azure Open AI</a> models and prompts. </h4>

<p align="center">
  <a href="#how-to-use">How To Use</a> •
  <a href="#credits">Credits</a> •
  <a href="#license">License</a> •
  <a href="#contact">Contact</a>
</p>

## Pre-req Azure components

This repo has all the code to perform the tests against [Azure Open AI](https://learn.microsoft.com/en-us/azure/ai-services/openai/overview). But you will need an Azure subscription with Azure Open AI enabled and your target models deployed. Instructions on how to do this can be found [here](https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/create-resource?pivots=cli)

## How To Use

To clone and run this application, you'll need [Git](https://git-scm.com) installed on your computer.

```bash
# Clone this repository
$ git clone https://github.com/fredderf204/aoai-tester

# Go into the repository
cd aoai-tester
```

Next open the code in your favourite editor, change the following parameters;

- target_model = the Azure Open AI model you wish to test
- api_key = Azure Open AI Key found in the Azure Portal
- azure_endpoint = Azure Open AI Endpoint found in the Azure Portal
- azure_deployment = The name of your model deployment

Then run the code :)

## Credits

This software uses the following open source packages:

- [Python](https://www.python.org/)
- [Azure Open AI](https://learn.microsoft.com/en-us/azure/ai-services/openai/overview)

## License

MIT License

Copyright (c) [2023] [Michael Friedrich]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

---

## Contact

> LinkedIn [Michael Friedrich](https://www.linkedin.com/in/1michaelfriedrich/) &nbsp;&middot;&nbsp;
> GitHub [fredderf204](https://github.com/fredderf204) &nbsp;&middot;&nbsp;
> Twitter [@fredderf204](https://twitter.com/fredderf204)