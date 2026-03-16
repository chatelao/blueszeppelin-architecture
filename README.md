# Blues Zeppelin Network Topology

This document describes the network, server, and application layout of the "Blues Zeppelin" podcast hosted by Mark Stenzler.

## Overview

"Blues Zeppelin" is a long-running radio program (since 1989) based in Bern, Switzerland. It is broadcast on terrestrial radio and distributed as a podcast.

## Infrastructure and Components

### 3. Servers
| Name | Function | IP Address | Source | Port 80 | Port 443 | Redirects / Proxy | Status |
|------|----------|------------|--------|---------|----------|-------------------|--------|
| `blueszeppelin.net` | Web / App Server | 91.207.255.224 | Direct | ❌ | ✅ | Meta-refresh to RaBe | Updated |
| `feed.blueszeppelin.net` | FeedBurner Proxy | 74.125.132.121 | Proxy | ✅ | ❌ | Proxies to Google/FeedBurner | Updated |
| `podcasts.apple.com` | Podcast Directory | 23.38.252.25 | Apple | ✅ | ✅ | None | Updated |
| `music.youtube.com` | Music/Podcast Service | 74.125.132.190 | Google | ✅ | ✅ | None | Updated |
| `rabe.ch` | Radio Station Site | 159.100.249.37 | RaBe | ✅ | ✅ | None | Updated |
| `nuxit.com` | Hosting Provider | 195.144.11.38 | Nuxit | ✅ | ✅ | None | Updated |

### 4. Software and Systems
| System | Source | Version | Security Flaws | Available Upgrades |
|--------|--------|---------|----------------|--------------------|
| Apache | nuxit.com | Unknown | Standard vulnerabilities (e.g. CVE-2023-25690) | Latest stable Apache 2.4.x |
| Podcast Generator | podcastgenerator.net | 2.6 | Lacks recent security patches | Podcast Generator 3.x |
| PHP | nuxit.com | Unknown | Dependent on server config | PHP 8.x (check compatibility) |

### 5. DNS Configuration

**Responsible Name Servers:** `ns1.modns.fr`, `ns2.modns.fr`

| Type | Entry | Value / Target | Function |
|------|-------|----------------|----------|
| A | `blueszeppelin.net` | `91.207.255.224` | Primary Web Server |
| A | `www.blueszeppelin.net` | `91.207.255.224` | WWW Redirect / Alias |
| CNAME | `feed.blueszeppelin.net` | `4n30s7.feedproxy.ghs.google.com` | FeedBurner RSS Proxy |
| MX | `blueszeppelin.net` | `mx.webmo.fr` (Pri 10) | Mail Exchange |
| NS | `blueszeppelin.net` | `ns1.modns.fr` | Primary Name Server |
| NS | `blueszeppelin.net` | `ns2.modns.fr` | Secondary Name Server |

### 6. Broadcast and Syndication
- **Primary Broadcast:** **Radio RaBe** (Radio Bern, 95.6 MHz) on Sunday afternoons.
- **Radio RaBe IP:** `159.100.249.37`
- **Syndication:** The program is also aired on:
    - Radio LoRa (Zurich, CH)
    - Diis Radio (Canton Valais, CH)
    - CJRO Community Radio (Ottawa, CAN)
    - WRFI Community Radio (Ithaca NY / Odessa NY, USA)
    - Ground Zero Radio Network (Portland OR, USA)

### 7. Online Presence
- **Homepage Redirect:** `https://blueszeppelin.net` often serves as a landing page or redirects to the Radio RaBe program page.
- **RaBe Program Page:** `https://rabe.ch/blues-zeppelin/` serves as the official radio station profile.
- **Social Media:** [Blues Zeppelin Facebook Page](https://www.facebook.com/BluesZeppelin)

## Topology Diagram

![Topology Diagram](https://www.plantuml.com/plantuml/png/ZLF1Rjf04BtlLumuL205jpWXKJbKYOjeL9M2SAfAJNiOx8bPONQjzJefgVhlcTrr3FHKNopFU_jcvhtrTMtHs6PN2YjjIP2K3TNmWwgAIgdWAzadRRPmfojTwc8lHBsLgaA3EyZqhjAAb4tjdayQoYogeYGXAiosM13qbaRdJMQbLZtu8u0VpAmsq9iZYwQMr7D9fWTOWwjundrgcrngU0ihTEyL9lJBCK9T_3tI_qvhICayae7--r4KlxkAul4uYkEBmMl3-njcRu82qmCx84kTPrXR-4IA3BgvukZI4ndXecVbQ76DDJURKowHfz26UuUPNULae1bHpgie_jYnCzqGhfuqXli0U_9x_rFrhowYKJoEHkSnlqS3ttUMdAWbHgCVaKpTIHrSuPt7qINCRv_3QLSBd8NTSAVKehE-XluNlS8p-FXvjJW3ibaK-9xbvKwwJcKXBPOmbRKrSjqSnyTkLfnrwrpjPNofdIrDuQOe31NEpW1ppSdxn8V33ssCC85mEVYsPLhnJR2YHHmf1C2aRrN97i1yUGvls6-BeeM6kNvIp0ofJ7mkhFKWIwf55tH7wmHlDSyjEfMcOd2MCE1cNnZUNK7_WUEAgaqr40m5JbYS--nLBZEqv1VhO7VwN_1u8P_N1Bf4XIyuv932aG1RBaHe-Rh1OQS9H-F-jdRtAUFE9E5c-7-sk2QLkn__1G00)

*(Note: The above diagram is rendered via the PlantUML server using the encoded source from `diagrams/topology.puml`.)*

## Data Flow

1. **Production:** Audio is produced (likely at Radio RaBe or a private studio).
2. **Upload:** MP3 files and metadata are uploaded to the **Podcast Generator** instance on `blueszeppelin.net`.
3. **RSS Generation:** Podcast Generator updates the RSS feed.
4. **Feed Polling:** **FeedBurner** polls the origin feed and updates `feed.blueszeppelin.net`.
5. **Distribution:**
    - **Apple Podcasts** and other aggregators poll FeedBurner.
    - Listeners download media directly from `blueszeppelin.net`.
