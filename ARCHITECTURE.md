# Architecture Notes

## Purpose

This repository contains the public website served on:

- `https://www.assps.edu.pk`

## Main Parts

- `index.html`
  - main entry for the static site
- `assets/`
  - bundled static assets
- `images/`
  - site imagery and public media

## Production Mapping

- live static root: `/var/www/apex-web`
- served directly by Nginx
- `/api/` traffic proxies to backend `127.0.0.1:5000`

## Repository Rule

- product-facing website files stay at the root and public asset folders
- one-off repair or screenshot helpers do not belong in the main content path long-term
- any operational helper should live under `ops/legacy/`

## Safety

- GitHub pushes do not change the live website automatically
- deploy only through an intentional separate release step
