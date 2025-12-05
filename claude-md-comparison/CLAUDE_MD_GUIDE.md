# CLAUDE.md 완벽 가이드

## 📋 CLAUDE.md란?

**Claude Code가 모든 세션마다 자동으로 읽어들이는 특수 파일**로, 프로젝트에 대한 지속적인 컨텍스트를 제공합니다.

### 핵심 개념
LLM은 상태를 저장하지 않기 때문에 매 세션마다 프로젝트를 처음 접하게 됩니다. CLAUDE.md는 "매 세션마다 코드베이스를 AI에게 소개하는 자동 온보딩 문서" 역할을 합니다.

### 해결하는 문제
- ✅ 매 세션마다 반복되는 프로젝트 설명 제거
- ✅ 토큰 비용 절감
- ✅ 일관된 작업 품질 유지
- ✅ 프로젝트 컨텍스트 자동 제공

---

## 📝 포함해야 할 내용

### 3가지 핵심 요소: WHAT, WHY, HOW

#### 1. WHAT (무엇)
- 기술 스택 (프레임워크, 언어, 도구)
- 프로젝트 구조 (디렉토리 구성)
- 파일 조직 (주요 파일의 역할)

#### 2. WHY (왜)
- 각 컴포넌트의 목적
- 설계 결정의 이유
- 아키텍처 선택 배경

#### 3. HOW (어떻게)
- 빌드 방법
- 테스트 실행 방법
- 개발 워크플로우
- 자주 사용하는 명령어

### 권장 섹션 구조

```markdown
# Tech Stack
# Project Overview
# Project Structure
# Commands
# Code Style
# Development Workflow
# Testing Strategy
# Do Not Section
```

---

## ✅ Best Practices

### 1. 간결함 유지 ⭐ (가장 중요!)

**권장 길이:**
- 300줄 미만 (필수)
- 60-100줄 (이상적)
- HumanLayer: 60줄 미만 유지

**이유:**
- LLM은 150-200개 지시사항만 효과적으로 처리 가능
- Claude Code 시스템 프롬프트에 이미 ~50개 지시사항 존재
- 소형 모델은 지시사항 증가 시 **지수적으로** 성능 저하

**작성 스타일:**
- ✅ 짧고 선언적인 글머리 기호 사용
- ✅ 한 줄에 하나의 개념
- ❌ 긴 서사적 문단 금지
- ❌ 불필요한 중복 제거

### 2. 보편적 적용성만 포함

**원칙:**
- 모든 세션에 적용되는 내용만 작성
- 특정 작업에만 필요한 내용은 제외

**주의:**
Claude는 관련 없다고 판단한 지시를 **무시할 수 있음**

시스템이 자동으로 추가하는 리마인더:
> "이 컨텍스트는 작업과 관련 없을 수 있으니 고도로 관련된 경우만 응답하세요"

### 3. Progressive Disclosure 패턴

**개념:** 세부 지침은 별도 파일로 분리

```
project-root/
├── CLAUDE.md                    # 핵심 정보만
└── agent_docs/
    ├── building_the_project.md
    ├── running_tests.md
    ├── code_conventions.md
    └── deployment_guide.md
```

**CLAUDE.md에서:**
```markdown
# Additional Documentation
- Building: See `agent_docs/building_the_project.md`
- Testing: See `agent_docs/running_tests.md`
- Conventions: See `agent_docs/code_conventions.md`
```

### 4. 파일 참조 선호

**코드 스니펫 대신 파일 참조 사용:**

❌ **나쁜 예:**
```markdown
## Authentication Pattern
```typescript
export async function authenticate(token: string) {
  // 30 lines of code...
}
```
```

✅ **좋은 예:**
```markdown
## Authentication Pattern
See `src/utils/auth.ts:45-60` for implementation details
```

**장점:**
- 파일 내용이 변경되어도 최신성 유지
- CLAUDE.md 길이 절약
- 필요할 때만 파일 읽기

### 5. 수작업으로 신중하게 작성

**중요:** CLAUDE.md는 "가장 높은 영향력 지점"

**작성 프로세스:**
1. `/init` 명령어로 초안 생성 (선택사항)
2. 모든 라인을 신중히 검토
3. 불필요한 내용 제거
4. 명확성과 간결성 확보
5. 팀과 공유하여 피드백 받기

❌ **하지 말 것:**
- 자동 생성 후 방치
- 검토 없이 그대로 사용
- 복사-붙여넣기로 급하게 작성

### 6. 강조 표현 활용

**모델 준수도 향상을 위한 키워드:**

```markdown
IMPORTANT: All new components must use TypeScript
YOU MUST: Run tests before committing
DO NOT: Modify files in the `legacy/` directory
NEVER: Commit directly to the main branch
ALWAYS: Use named exports instead of default exports
```

**효과:** 이러한 강조 표현은 Claude의 지시 준수율을 높입니다.

### 7. 반복적 개선

**지속적 관리 방법:**

1. **실시간 업데이트:** 작업 중 `#` 키를 눌러 CLAUDE.md에 추가
2. **오류 기반 개선:** Claude가 반복하는 실수를 문서화
3. **팀 피드백:** 팀원들의 경험 반영
4. **프로젝트 진화:** 기술 스택 변경 시 즉시 업데이트

**주의:** "한 번 작성하고 잊어버리기"는 최악의 접근법

### 8. 명시적 구조화

**마크다운 제목으로 논리적 섹션 구성:**

```markdown
# Tech Stack
## Frontend
## Backend
## Database

# Project Structure
## Source Files
## Test Files
## Configuration

# Commands
## Development
## Testing
## Deployment
```

---

## ❌ 하지 말아야 할 것

### 1. 스타일 가이드 포함 금지

**원칙:** "Claude는 린터가 아닙니다"

❌ **CLAUDE.md에 넣지 말 것:**
```markdown
- Use 2 spaces for indentation
- Always use semicolons
- Maximum line length: 80 characters
- Use single quotes instead of double quotes
```

✅ **대신 사용할 도구:**
- Prettier (자동 포맷팅)
- ESLint (린팅)
- `.editorconfig` (에디터 설정)

**CLAUDE.md에는 도구 사용 지시만:**
```markdown
IMPORTANT: Run `npm run lint` before committing
```

### 2. 과도한 지시사항

**한계:**
- Claude 시스템 프롬프트: ~50개 지시
- CLAUDE.md: 최대 100-150개 지시
- **합계: 150-200개 이내 유지**

❌ **피해야 할 것:**
- 모든 함수 네이밍 규칙 나열
- 세세한 코딩 패턴 100가지
- 모든 예외 케이스 문서화

### 3. 장황한 설명

❌ **나쁜 예:**
```markdown
This project uses React, which is a JavaScript library
for building user interfaces. It was created by Facebook
and is widely used in the industry. We chose React because
it provides a component-based architecture that makes it
easier to build and maintain complex UIs...
```

✅ **좋은 예:**
```markdown
- Framework: React 18
- Why: Component-based architecture, strong ecosystem
```

### 4. 특정 작업 전용 정보

❌ **보편적이지 않은 내용:**
```markdown
- When fixing the login bug, check the session timeout
- For the Q4 feature, use the new API endpoint
- Bob's code in utils.ts needs refactoring
```

✅ **보편적인 내용:**
```markdown
- Authentication: See src/auth/ directory
- API endpoints: Defined in src/api/routes.ts
- Code quality: Run `npm run lint` to check
```

### 5. 한 번 작성 후 방치

❌ **문제가 되는 상황:**
- 프로젝트는 Next.js 14로 업그레이드 → CLAUDE.md는 여전히 Next.js 12
- 테스트 프레임워크를 Jest에서 Vitest로 변경 → CLAUDE.md 미반영
- 새로운 모노레포 구조 도입 → CLAUDE.md 업데이트 안 됨

✅ **올바른 접근:**
- 주요 기술 스택 변경 시 즉시 업데이트
- 월 1회 정기 검토
- 팀원 온보딩 시 함께 검토

---

## 📂 파일 배치 위치

### 우선순위 순서 (높음 → 낮음)

```
1. 현재 작업 디렉토리
   ./CLAUDE.md

2. 상위 디렉토리 (monorepo 지원)
   ../CLAUDE.md
   ../../CLAUDE.md

3. 프로젝트 루트
   /project-root/CLAUDE.md

4. 홈 폴더 (전역 설정)
   ~/.claude/CLAUDE.md
```

### 다중 CLAUDE.md 전략

**Monorepo 예시:**
```
monorepo-root/
├── CLAUDE.md                 # 전체 구조, 공통 규칙
├── apps/
│   ├── web/
│   │   └── CLAUDE.md         # Next.js 앱 특화 정보
│   └── api/
│       └── CLAUDE.md         # Express API 특화 정보
└── packages/
    └── shared/
        └── CLAUDE.md         # 공유 패키지 정보
```

**효과:**
- 작업 위치에 따라 적절한 컨텍스트 자동 로드
- 하위 디렉토리의 CLAUDE.md가 상위 내용 보완

### 개인 설정 분리

```
project/
├── CLAUDE.md                 # 팀 공유 (Git에 커밋)
└── CLAUDE.local.md           # 개인 설정 (.gitignore)
```

**CLAUDE.local.md 용도:**
- 개인 워크플로우 선호
- 로컬 환경 특화 설정
- 실험적 지시사항

---

## 💡 실제 예시

### 예시 1: 간단한 프로젝트

```markdown
# Tech Stack
- Framework: Next.js 14
- Language: TypeScript 5.2
- Styling: Tailwind CSS 3.4
- Database: PostgreSQL with Prisma

# Project Structure
- `src/app`: Next.js App Router pages
- `src/components`: Reusable React components
- `src/lib`: Core utilities and API clients
- `prisma/`: Database schema and migrations

# Commands
- `npm run dev`: Start development server (port 3000)
- `npm run build`: Production build
- `npm test`: Run Jest tests
- `npx prisma migrate dev`: Run database migrations

# Code Style
IMPORTANT: Use ES modules (import/export)
- All components must be function components with Hooks
- Prefer arrow functions for component definitions
- Use named exports (no default exports)

# Testing
YOU MUST: Write tests for all new features
- Unit tests: `__tests__/` directory
- Coverage requirement: 80%

# Do Not
- DO NOT edit files in `src/legacy` directory
- DO NOT commit directly to `main` branch
- NEVER expose API keys in client-side code
```

### 예시 2: Monorepo 루트

```markdown
# Monorepo Overview
Full-stack application with shared packages

## Workspace Structure
- `apps/web`: Next.js frontend
- `apps/api`: Express.js backend
- `packages/shared`: Shared TypeScript utilities
- `packages/ui`: Shared React components

# Tech Stack
- Package Manager: pnpm
- Monorepo Tool: Turborepo
- TypeScript: 5.2 (workspace-wide)

# Commands
- `pnpm install`: Install all dependencies
- `pnpm build`: Build all packages
- `pnpm dev`: Run all apps in development mode
- `pnpm test`: Run all tests

# Development Workflow
1. Create feature branch from `develop`
2. Make changes in relevant workspace
3. Run `pnpm test` before committing
4. Create PR to `develop` branch

# Important Notes
IMPORTANT: Run commands from monorepo root
- Changes in `packages/` affect multiple apps
- Always update affected app tests when changing shared packages

# Additional Docs
- Web app: `apps/web/CLAUDE.md`
- API: `apps/api/CLAUDE.md`
- Contributing: `CONTRIBUTING.md`
```

### 예시 3: Python 프로젝트

```markdown
# Tech Stack
- Language: Python 3.11
- Framework: FastAPI 0.104
- Database: PostgreSQL + SQLAlchemy
- Testing: pytest

# Project Structure
- `src/api/`: FastAPI endpoints
- `src/models/`: SQLAlchemy models
- `src/services/`: Business logic
- `tests/`: pytest test suite

# Environment Setup
```bash
python -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows
pip install -r requirements.txt
```

# Commands
- `uvicorn src.main:app --reload`: Development server
- `pytest`: Run all tests
- `pytest --cov`: Run tests with coverage
- `alembic upgrade head`: Run database migrations

# Code Style
IMPORTANT: Follow PEP 8
- Use type hints for all function signatures
- Maximum line length: 88 characters (Black default)
- Run `black .` and `isort .` before committing

# Testing
YOU MUST: Maintain 80%+ test coverage
- Use pytest fixtures for database setup
- Mock external API calls
- Test both success and error cases

# Do Not
- DO NOT commit `.env` files
- DO NOT use `print()` for logging (use `logger` instead)
- NEVER skip database migrations
```

---

## 🎯 핵심 통찰

### CLAUDE.md의 본질

> "CLAUDE.md는 단순한 문서가 아니라 모든 세션의 초기 프롬프트를 커스터마이즈하는 고영향 도구입니다"

### 비유로 이해하기

**CLAUDE.md는:**
- 회사의 신입 개발자에게 첫날 30분 안에 설명할 핵심 내용
- 정기적인 상기가 필요한 주니어 개발자에게 주는 체크리스트
- 프로젝트 온보딩 세션의 핵심 슬라이드

### 작성 철학

**"Less is More"**
- 짧고
- 명확하고
- 보편적으로 적용 가능하게

**"Progressive Disclosure"**
- 핵심만 CLAUDE.md에
- 세부사항은 별도 파일로

**"Living Document"**
- 지속적으로 업데이트
- 팀과 함께 개선
- 프로젝트와 함께 진화

---

## 🛠️ 실전 워크플로우

### 1. 초기 작성

```bash
# 1. Claude Code에서 초안 생성
/init

# 2. 생성된 CLAUDE.md 검토
# 3. 불필요한 내용 제거
# 4. 핵심 정보 추가
# 5. 팀원과 리뷰
```

### 2. 작업 중 업데이트

```bash
# 작업 중 Claude Code에서 # 키 누르기
# → 새로운 지시사항 추가
# → CLAUDE.md에 자동 반영
```

### 3. 정기 유지보수

**월간 체크리스트:**
- [ ] 기술 스택 버전이 최신인가?
- [ ] 프로젝트 구조가 정확한가?
- [ ] 명령어들이 여전히 작동하는가?
- [ ] 새로운 팀원이 이해하기 쉬운가?
- [ ] 불필요한 내용이 있는가?

### 4. 효과 측정

**개선 여부 확인:**
- Claude의 첫 응답 정확도
- 반복 질문 감소 여부
- 코드 일관성 향상
- 온보딩 시간 단축

---

## 📚 참고 자료

### 공식 문서
- [Anthropic: Claude Code Best Practices](https://www.anthropic.com/engineering/claude-code-best-practices)
- [Claude.com: Using CLAUDE.MD files](https://www.claude.com/blog/using-claude-md-files)

### 심화 가이드
- [HumanLayer: Writing a good CLAUDE.md](https://www.humanlayer.dev/blog/writing-a-good-claude-md)
- [Apidog: What's a Claude.md File? 5 Best Practices](https://apidog.com/blog/claude-md/)
- [Maxitect: Building an Effective CLAUDE.md](https://www.maxitect.blog/posts/maximising-claude-code-building-an-effective-claudemd)
- [Shuttle: Claude Code Best Practices](https://www.shuttle.dev/blog/2025/10/16/claude-code-best-practices)

### 커뮤니티 자료
- [Sabrina.dev: The ULTIMATE AI Coding Guide](https://www.sabrina.dev/p/ultimate-ai-coding-guide-claude-code)
- [htdocs.dev: Claude Code Best Practices and Pro Tips](https://htdocs.dev/posts/claude-code-best-practices-and-pro-tips/)
- [Sid Bharath: Cooking with Claude Code](https://www.siddharthbharath.com/claude-code-the-complete-guide/)

---

## ✨ 요약 체크리스트

작성 전 확인사항:
- [ ] 300줄 미만으로 유지
- [ ] WHAT, WHY, HOW 포함
- [ ] 보편적으로 적용 가능한 내용만
- [ ] 강조 표현 (IMPORTANT, DO NOT) 사용
- [ ] 코드 스니펫 대신 파일 참조
- [ ] 스타일 가이드 제외 (린터 사용)
- [ ] 세부사항은 별도 파일로 분리
- [ ] 팀원과 리뷰 완료
- [ ] Git에 커밋 (.gitignore 확인)

작성 후 확인사항:
- [ ] Claude가 프로젝트를 빠르게 이해하는가?
- [ ] 반복 질문이 줄어들었는가?
- [ ] 코드 일관성이 향상되었는가?
- [ ] 신규 팀원 온보딩이 쉬워졌는가?

---

**마지막 조언:**

CLAUDE.md는 "완벽한 문서"가 아니라 "유용한 도구"입니다.
완벽을 추구하지 말고, 실용성을 우선하세요.

**시작은 간단하게, 개선은 지속적으로!** 🚀
