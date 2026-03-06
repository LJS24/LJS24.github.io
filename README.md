# LJS24.github.io

학습 기록(`learn`), 프로젝트 공유(`projects`), 리서치 보고(`research`)를 위한 Jekyll 기반 블로그입니다.

## 1) 프로젝트 구조

```text
.
├─ _config.yml                    # 사이트 설정 (permalink, markdown, defaults)
├─ _data/
│  └─ bibliography.yml
├─ _drafts/                       # 초안(게시 전)
├─ _layouts/
│  ├─ default.html                # 공통 레이아웃
│  └─ post.html                   # 게시물 레이아웃
├─ _includes/
│  ├─ nav.html
│  └─ post-list.html
├─ _posts/
│  ├─ learn/                      # 학습 노트
│  ├─ projects/                   # 프로젝트 공유
│  └─ research/                   # 리서치 보고
├─ templates/                     # 새 글 작성용 템플릿 원본
│  ├─ learn.md
│  ├─ project.md
│  └─ research.md
├─ docs/
│  └─ writing-guidelines.md       # 작성 원칙 (근거/인용 정책)
├─ assets/
│  ├─ css/site.css
│  ├─ images/                     # 이미지 파일 저장
│  └─ diagrams/                   # 다이어그램 파일 저장
├─ index.md                       # 메인 페이지
├─ learn.md                       # learn 목록 페이지
├─ projects.md                    # projects 목록 페이지
├─ research.md                    # research 목록 페이지
└─ .github/workflows/pages.yml    # GitHub Pages 빌드/배포
```

## 2) 게시물 작성 규칙

### 파일 위치/이름
- 학습 노트: `_posts/learn/YYYY-MM-DD-title.md`
- 프로젝트 공유: `_posts/projects/YYYY-MM-DD-title.md`
- 리서치 보고: `_posts/research/YYYY-MM-DD-title.md`

### Front Matter 공통 필드
```yaml
---
title: "게시물 제목"
date: YYYY-MM-DD
categories: [learn]
tags: []
summary: "요약"
---
```

카테고리에 따라 `categories` 값만 `learn`, `projects`, `research` 중 하나로 바꿔 사용합니다.

`_config.yml`에서 모든 post 기본 레이아웃은 `layout: post`가 적용됩니다.

### 카테고리별 권장 필드
- `learn`: `level` (예: beginner/intermediate/advanced)
- `projects`: `repo` (GitHub 저장소 URL)
- `research`: 재현성 관련 섹션(`Reproducibility`) 필수 권장

## 3) 템플릿 사용 방법

현재 템플릿 파일:
- `_posts/learn/2026-02-19-learning-note-template.md`
- `_posts/projects/2026-02-19-project-post-template.md`
- `_posts/research/2026-02-19-research-report-template.md`
- `templates/learn.md`
- `templates/project.md`
- `templates/research.md`

작성 절차:
1. 카테고리에 맞는 템플릿을 복사합니다.
2. 파일명을 `YYYY-MM-DD-title.md` 형식으로 저장합니다.
3. Front Matter (`title`, `date`, `categories`, `summary`, `tags`)를 수정합니다.
4. 본문 섹션을 실제 내용으로 채우고 `References`를 반드시 작성합니다.

## 4) 이미지/영상 첨부 가이드

### 이미지
- 저장 위치: `assets/images/<category>/<post-slug>/...`
- 삽입 예시:

```md
![설명 텍스트]({{ '/assets/images/learn/my-post/example.png' | relative_url }})
```

### 다이어그램
- 저장 위치: `assets/diagrams/<category>/<post-slug>/...`
- 삽입 예시:

```md
![시스템 다이어그램]({{ '/assets/diagrams/projects/my-post/architecture.svg' | relative_url }})
```

### 외부 영상(YouTube 등)
- 기본은 링크 첨부 권장
- 임베드가 필요하면 HTML `iframe` 사용

```html
<iframe width="560" height="315"
  src="https://www.youtube.com/embed/VIDEO_ID"
  title="YouTube video player" frameborder="0" allowfullscreen></iframe>
```

### 로컬 영상(mp4 등)
- 필요 시 `assets/videos/...` 디렉터리를 추가해서 사용

```html
<video controls preload="metadata" style="width:100%;max-width:960px;">
  <source src="{{ '/assets/videos/projects/my-post/demo.mp4' | relative_url }}" type="video/mp4">
</video>
```

## 5) 작성 가이드라인 (docs/writing-guidelines.md)

원칙:
- 공식 문서/논문 등 신뢰 가능한 근거 우선
- 검증되지 않은 주장은 가설로 명시
- 연구/프로젝트 글은 재현 가능한 절차 포함
- 모든 글에 출처 링크 포함

## 6) URL/배포 동작

- Permalink 패턴: `/:categories/:year/:month/:day/:title/`
- GitHub Actions(`.github/workflows/pages.yml`)로 `main` 브랜치 push 시 빌드/배포
- 배포 전 `_site`, `README.md`, `docs` 대상 링크 점검(lychee) 수행
