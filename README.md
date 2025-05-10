# XAL Reversal – Epic Games hCaptcha Data Extraction

## Overview

This project documents the successful reverse engineering of the `xal` value, a key component in the data collection and submission pipeline used by Epic Games in conjunction with hCaptcha for bot mitigation.

Through reverse engineering, I discovered how `xal` is generated and structured. This value plays a crucial role in the communication between the client browser and hCaptcha, encapsulating behavior data in a format expected by Epic’s anti-bot system. By understanding and reconstructing this value, it is possible to simulate or inspect the data blob submitted to hCaptcha on behalf of the Epic Games login page.

## Purpose

The goal of this research was to:

- Understand the role of `xal` in the client-server communication process for hCaptcha integration on Epic Games.
- Reproduce a valid `xal` payload to analyze the behavioral telemetry it encapsulates.
- Lay the groundwork for further analysis of anti-bot fingerprinting mechanisms used on modern websites.

## Disclaimer

This project is for **educational and research purposes only**. Do not use this knowledge or any derivative work for unauthorized access or any activity that violates the terms of service of any platform. Always obtain proper authorization when performing security research.

