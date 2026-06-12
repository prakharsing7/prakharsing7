<a id="readme-top"></a>

[![LinkedIn][linkedin-shield]][linkedin-url]
[![Portfolio][portfolio-shield]][portfolio-url]
[![Email][email-shield]][email-url]

<div align="center">
  <h1>👋 Hi, I'm Prakhar Singh</h1>
  <p><em>AI &amp; Backend Engineer &nbsp;·&nbsp; Building open-source EV smart charging at Electric Miles</em></p>
</div>

---

## About Me

I'm a researcher and platform engineer at [Electric Miles](https://electricmiles.com), where I investigate the gap between OCPP smart charging specifications and real-world grid-responsive behaviour. My work sits at the intersection of energy systems, convex optimisation, and distributed software — turning grid constraints and price signals into OCPP-native charging schedules that run on real hardware.

When I'm not optimising EV fleets, I'm probably poking at computer vision, physics simulations, or building things that are harder than they should be.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## 🔋 What I'm Building

### [GridMind](https://github.com/prakharsing7/gridmind)
> Optimal EV charging schedules via convex LP, output as OCPP-native `SetChargingProfile` messages ready to send to real chargers.

```text
EV sessions + grid constraints + price signal
                ↓
       CVXPY LP optimiser
  (minimise cost · SoC + power + feeder limits)
                ↓
  OCPP SetChargingProfile.req JSON
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## 🛠 Tech Stack

[![Python][python-shield]][python-url]
[![TypeScript][ts-shield]][ts-url]
[![Next.js][next-shield]][next-url]
[![CVXPY][cvxpy-shield]][cvxpy-url]
[![Docker][docker-shield]][docker-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## 📊 GitHub Stats

<div align="center">
  <img height="160" src="https://github-readme-stats.vercel.app/api?username=prakharsing7&show_icons=true&theme=github_dark&hide_border=true" alt="GitHub Stats" />
  &nbsp;
  <img height="160" src="https://github-readme-stats.vercel.app/api/top-langs/?username=prakharsing7&layout=compact&theme=github_dark&hide_border=true&langs_count=6" alt="Top Languages" />
</div>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## 📬 Connect

[![LinkedIn][linkedin-shield]][linkedin-url] &nbsp; [![Portfolio][portfolio-shield]][portfolio-url] &nbsp; [prakhar@electricmiles.com](mailto:prakhar@electricmiles.com)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

<!-- REFERENCE LINKS -->
[linkedin-shield]: https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white
[linkedin-url]: https://linkedin.com/in/prakharsingh10
[portfolio-shield]: https://img.shields.io/badge/Portfolio-000000?style=for-the-badge&logo=vercel&logoColor=white
[portfolio-url]: https://prakharsing7.vercel.app
[email-shield]: https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white
[email-url]: mailto:prakhar@electricmiles.com
[python-shield]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[python-url]: https://python.org
[ts-shield]: https://img.shields.io/badge/TypeScript-007ACC?style=for-the-badge&logo=typescript&logoColor=white
[ts-url]: https://typescriptlang.org
[next-shield]: https://img.shields.io/badge/Next.js-000000?style=for-the-badge&logo=next.js&logoColor=white
[next-url]: https://nextjs.org
[cvxpy-shield]: https://img.shields.io/badge/CVXPY-FF6F00?style=for-the-badge&logo=python&logoColor=white
[cvxpy-url]: https://cvxpy.org
[docker-shield]: https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white
[docker-url]: https://docker.com
