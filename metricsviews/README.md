#

<p align="center">
  <img src="../logo/metricsviews.png" width="100%">
  <h1 align="center">
    Metricsviews Frontend
  </h1>
<p align="center">An Open Source MultiCloud Loadbalancer and MetricsMonitor.</p>
</p>

<div align="center">
  
<a href="https://metricsviews.com">![METRICSVIEWS](https://img.shields.io/badge/Metricsviews-Live%20Demo-9cf?style=for-the-badge)</a>
<a href="#">![Metricsviews UI Kit](https://img.shields.io/badge/Metricsviews-UI%20Kit-orange?style=for-the-badge)</a>
<a href="https://discord.gg/jzJ57c8533">![Metricsviews Community](https://img.shields.io/discord/842133683037012039?label=Metricsviews%20Community&style=for-the-badge&logo=Discord)</a>

</div>
<p>

# metricsviews

> MultiCloud Loadbalancer And  MetricsMonitor

## Features

```
- Login / Logout

- Permission Authentication
  - Page permission
  - Directive permission
  - Permission configuration page
  - Two-step login

- Multi-environment build
  - Develop (dev)
  - sit
  - Stage Test (stage)
  - Production (prod)

- Global Features
  - I18n
  - Multiple dynamic themes
  - Dynamic sidebar (supports multi-level routing)
  - Dynamic breadcrumb
  - Tags-view (Tab page Support right-click operation)
  - Svg Sprite
  - Mock data
  - Screenfull
  - Responsive Sidebar

- Editor
  - Rich Text Editor
  - Markdown Editor
  - JSON Editor

- Excel
  - Export Excel
  - Upload Excel
  - Visualization Excel
  - Export zip

- Table
  - Dynamic Table
  - Drag And Drop Table
  - Inline Edit Table

- Error Page
  - 401
  - 404

- Components
  - Avatar Upload
  - Back To Top
  - Drag Dialog
  - Drag Select
  - Drag Kanban
  - Drag List
  - SplitPane
  - Dropzone
  - Sticky
  - CountTo

- Advanced Example
- Error Log
- Dashboard
- Guide Page
- ECharts
- Clipboard
- Markdown to html
```

## Getting started

```bash
# clone the project
git clone https://github.com/nik0811/metricsviews.git

# enter the project directory
cd metricsviews

# install dependency
npm install

# develop
npm run dev
```

This will automatically open http://localhost:9527

## Build

```bash
# build for test environment
npm run build:stage

# build for production environment
npm run build:prod
```

## Advanced

```bash
# preview the release environment effect
npm run preview

# preview the release environment effect + static resource analysis
npm run preview -- --report

# code format check
npm run lint

# code format check and auto fix
npm run lint -- --fix
```
