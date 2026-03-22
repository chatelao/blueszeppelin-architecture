# Blues Zeppelin Network Topology

This document describes the network, server, and application layout of the "Blues Zeppelin" podcast hosted by Mark Stenzler.

## Overview

"Blues Zeppelin" is a long-running radio program (since 1989) based in Bern, Switzerland. It is broadcast on terrestrial radio and distributed as a podcast.

## Infrastructure and Components

### 3. Servers
| Name | Function | Admin URL | IP Address | Source | Port 80 | Port 443 | Redirects / Proxy |
|------|----------|-----------|------------|--------|---------|----------|-------------------|
| `blueszeppelin.net` | Web / App Server | [Admin](https://blueszeppelin.net/podcast/?p=admin) | 188.130.25.202 | Direct | ✅ | ✅ | Meta-refresh to RaBe |
| `feed.blueszeppelin.net` | FeedBurner Proxy | [Admin](https://feedburner.google.com/) | 173.194.206.121 | Proxy | ✅ | ✅ | Proxies to Google/FeedBurner |
| `podcasts.apple.com` | Podcast Directory | [Admin](https://podcastsconnect.apple.com/) | 2.16.232.30 | Apple | ✅ | ✅ | None |
| `music.youtube.com` | Music/Podcast Service | [Admin](https://studio.youtube.com/) | 74.125.126.136 | Google | ✅ | ✅ | None |
| `rabe.ch` | Radio Station Site | [Admin](https://data.rabe.ch/admin/) | 159.100.249.37 | RaBe | ✅ | ✅ | None |
| `nuxit.com` | Hosting Provider | [Admin](https://cp.nuxit.com/) | 195.144.11.38 | Nuxit | ✅ | ✅ | None |

### 4. Software and Systems
| System | Source | Version | Security Flaws | Available Upgrades |
|--------|--------|---------|----------------|--------------------|
| Apache | nuxit.com | Unknown | Standard vulnerabilities (e.g. CVE-2023-25690) | Latest stable Apache 2.4.x |
| Podcast Generator | podcastgenerator.net | 2.6 | Lacks recent security patches | Podcast Generator 3.x |
| PHP | nuxit.com | Unknown | Dependent on server config | PHP 8.x (check compatibility) |

### 5. DNS Configuration

**Registrar:** [domain.com](https://www.domain.com)

**Responsible Name Servers:** `ns1.modns.fr`, `ns2.modns.fr`

| Type | Entry | Value / Target | Function |
|------|-------|----------------|----------|
| A | `blueszeppelin.net` | `188.130.25.202` | Primary Web Server |
| A | `www.blueszeppelin.net` | `188.130.25.202` | WWW Redirect / Alias |
| CNAME | `feed.blueszeppelin.net` | `4n30s7.feedproxy.ghs.google.com` | FeedBurner RSS Proxy |
| MX | `blueszeppelin.net` | `mx.webmo.fr` (Pri 10) | Mail Exchange |
| NS | `blueszeppelin.net` | `ns1.modns.fr` | Primary Name Server |
| NS | `blueszeppelin.net` | `ns2.modns.fr` | Secondary Name Server |

## Topology Diagram

![Topology Diagram](https://www.plantuml.com/plantuml/png/ZPH1Rnen48Nl_XKZ3XKSs9PDQ5GELK28fWSQn59LRTg3sHqMYyMsl7QJJTN_th6zR99AaU2oCEzvvlaRuBgst5Xth9WLjaAOLGvh-85QOoKaV45xhym1DaghIfKDO_L1ICqDFqAkZbf9b3Qp3Pqqc5ikomePqpm_y1AXjpAgSBaLIlRW3mDwyTmg0xqbfwQPHVbOeUa1hy5NWkCkiwuG2jx2clldci_mbtV4EllxhFytt4A6vZSQw7yO9UcxgoGTZvCqlHoS1jvDoRsF7SWUtL5PgIBdjOLFAD5mdojDtWSZALGChe9RlkKr3LjY8JYbK8Pcnyo-yYBG0h6WgqZwS2GoNGXVdpb3Su2OF3G_PV_gCXcbusHqaT9pD0Xp5xCNtUQY59PNC1UrDMBhdeEaUscYtjwX3iT3AQhVbTkuBSBIrI8FObjf6MjbnQuXoDCZVrIItcoSnCyoM6_j7isDszRHlCuoc9QbmT93YgEevgE6FGw77zlbm0JYokaxb2j9-xMiLRmfOYNJLrqfJg1M5_26A5hEMcbOg7j9piXw4cXJhvsei6RT-ZfRr_164GFMTN6QnCMC19_zrX172VqTBI7HUprW94LFX4Xp6bc8d5iC5-la4yLN3Hsfroq-mVyYYtDFrtYws8HsxNz8BO0vwPuKEmKv_yHJilFF-AZdkzaroiB_S_m3)

*(Note: The above diagram is rendered via the PlantUML server using the encoded source from `diagrams/topology.puml`.)*

## Data Flow

1. **Production:** Audio is produced (likely at Radio RaBe or a private studio).
2. **Upload:** MP3 files and metadata are uploaded to the **Podcast Generator** instance on `blueszeppelin.net`.
3. **RSS Generation:** Podcast Generator updates the RSS feed.
4. **Feed Polling:** **FeedBurner** polls the origin feed and updates `feed.blueszeppelin.net`.
5. **Distribution:**
    - **Apple Podcasts** and other aggregators poll FeedBurner.
    - Listeners download media directly from `blueszeppelin.net`.

## Podcast Hubs and Distribution

The "Blues Zeppelin" podcast is syndicated across various digital platforms and hubs:

| Hub | Description | Access Link |
|-----|-------------|-------------|
| **Apple Podcasts** | Primary podcast directory for Apple users. | [Listen on Apple Podcasts](https://podcasts.apple.com/ca/podcast/the-blueszeppelin-hosted-by-mark-stenzler-has-been/id1046574635) |
| **YouTube Music** | Integrated music and podcast service from Google. | [Listen on YouTube Music](https://music.youtube.com/search?q=The+BluesZeppelin) |
| **Spotify** | Global music and podcast streaming platform. | [Search on Spotify](https://open.spotify.com/search/The%20BluesZeppelin) |
| **Amazon Music** | Podcast and music hub for Amazon users. | [Search on Amazon Music](https://music.amazon.com/search/The+BluesZeppelin) |
| **TuneIn** | Radio and podcast streaming platform. | [Search on TuneIn](https://tunein.com/search/?query=The%20BluesZeppelin) |
| **Podcast Addict** | Popular Android podcast application. | [Search on Podcast Addict](https://podcastaddict.com/search?q=The+BluesZeppelin) |
