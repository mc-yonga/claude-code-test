---
name: test-minimal-coder-swarm
description: "동일한 minimal-coder 에이전트를 5개 인스턴스로 병렬 spawn하고, 각 인스턴스에 5개씩 sub-task 할당"
allowed-tools: Read, Write, Edit, Grep, Glob, Bash, TodoWrite, AskUserQuestion, Task
model: inherit
---

# Minimal Coder Swarm 테스트

동일한 minimal-coder 에이전트를 5개 인스턴스로 병렬 spawn하여, 각 인스턴스가 5개의 sub-task를 독립적으로 처리하는지 테스트합니다.

테스트 대상: $ARGUMENTS

---

## 개념 설명

### Swarm 패턴 적용

일반적인 swarm 패턴:
- researcher, coder, tester 등 서로 다른 에이전트 타입을 spawn

이 테스트의 패턴:
- 동일한 minimal-coder 에이전트를 5개 인스턴스로 spawn
- 각 인스턴스는 독립적인 context에서 5개의 sub-task를 처리
- 모든 인스턴스가 병렬로 동시 실행

구조:
```
[단일 메시지에서 5개 Task 동시 실행]
    │
    ├── Task 1 (minimal-coder 인스턴스 #1)
    │   ├── Sub-task 1-1
    │   ├── Sub-task 1-2
    │   ├── Sub-task 1-3
    │   ├── Sub-task 1-4
    │   └── Sub-task 1-5
    │
    ├── Task 2 (minimal-coder 인스턴스 #2)
    │   ├── Sub-task 2-1
    │   ├── Sub-task 2-2
    │   ├── Sub-task 2-3
    │   ├── Sub-task 2-4
    │   └── Sub-task 2-5
    │
    ├── Task 3 (minimal-coder 인스턴스 #3)
    │   ├── Sub-task 3-1
    │   ├── Sub-task 3-2
    │   ├── Sub-task 3-3
    │   ├── Sub-task 3-4
    │   └── Sub-task 3-5
    │
    ├── Task 4 (minimal-coder 인스턴스 #4)
    │   ├── Sub-task 4-1
    │   ├── Sub-task 4-2
    │   ├── Sub-task 4-3
    │   ├── Sub-task 4-4
    │   └── Sub-task 4-5
    │
    └── Task 5 (minimal-coder 인스턴스 #5)
        ├── Sub-task 5-1
        ├── Sub-task 5-2
        ├── Sub-task 5-3
        ├── Sub-task 5-4
        └── Sub-task 5-5
```

총계:
- Main Task: 5개 (병렬 실행)
- Sub-task per Main Task: 5개
- 전체 Sub-task: 25개

---

## 실행 워크플로우

### 1단계: 출력 디렉토리 준비

```bash
mkdir -p spawn-test/output/instance-{1,2,3,4,5}
```

### 2단계: 5개의 minimal-coder 인스턴스 병렬 spawn

반드시 아래 5개의 Task() 호출을 단일 메시지에서 동시에 실행:

```
[단일 메시지 - 5개 minimal-coder 인스턴스 병렬 spawn]:

Task(subagent_type="minimal-coder", prompt="""
INSTANCE_ID: 1
OUTPUT_DIR: spawn-test/output/instance-1/

## Main Task 1: 사칙연산 모듈 구현

다음 5개의 sub-task를 순서대로 처리하세요.

### Sub-task 1-1: add.py
두 숫자를 받아 합을 반환하는 함수

### Sub-task 1-2: subtract.py
두 숫자를 받아 차를 반환하는 함수

### Sub-task 1-3: multiply.py
두 숫자를 받아 곱을 반환하는 함수

### Sub-task 1-4: divide.py
두 숫자를 받아 몫을 반환하는 함수

### Sub-task 1-5: calculator.py
위 4개 함수를 통합한 Calculator 클래스

각 파일 하단에 테스트 코드 포함 (사용자 수정 가능한 테스트 변수 섹션 필수)
""")

Task(subagent_type="minimal-coder", prompt="""
INSTANCE_ID: 2
OUTPUT_DIR: spawn-test/output/instance-2/

## Main Task 2: 문자열 유틸리티 모듈 구현

다음 5개의 sub-task를 순서대로 처리하세요.

### Sub-task 2-1: reverse.py
문자열을 뒤집는 함수

### Sub-task 2-2: uppercase.py
문자열을 대문자로 변환하는 함수

### Sub-task 2-3: lowercase.py
문자열을 소문자로 변환하는 함수

### Sub-task 2-4: length.py
문자열 길이를 반환하는 함수

### Sub-task 2-5: string_utils.py
위 4개 함수를 통합한 StringUtils 클래스

각 파일 하단에 테스트 코드 포함 (사용자 수정 가능한 테스트 변수 섹션 필수)
""")

Task(subagent_type="minimal-coder", prompt="""
INSTANCE_ID: 3
OUTPUT_DIR: spawn-test/output/instance-3/

## Main Task 3: 리스트 통계 모듈 구현

다음 5개의 sub-task를 순서대로 처리하세요.

### Sub-task 3-1: sum_list.py
숫자 리스트의 합계를 반환하는 함수

### Sub-task 3-2: avg_list.py
숫자 리스트의 평균을 반환하는 함수

### Sub-task 3-3: max_list.py
숫자 리스트의 최대값을 반환하는 함수

### Sub-task 3-4: min_list.py
숫자 리스트의 최소값을 반환하는 함수

### Sub-task 3-5: list_stats.py
위 4개 함수를 통합한 ListStats 클래스

각 파일 하단에 테스트 코드 포함 (사용자 수정 가능한 테스트 변수 섹션 필수)
""")

Task(subagent_type="minimal-coder", prompt="""
INSTANCE_ID: 4
OUTPUT_DIR: spawn-test/output/instance-4/

## Main Task 4: 파일 유틸리티 모듈 구현

다음 5개의 sub-task를 순서대로 처리하세요.

### Sub-task 4-1: read_file.py
파일 내용을 읽어 반환하는 함수

### Sub-task 4-2: write_file.py
파일에 내용을 쓰는 함수

### Sub-task 4-3: file_exists.py
파일 존재 여부를 반환하는 함수

### Sub-task 4-4: delete_file.py
파일을 삭제하는 함수

### Sub-task 4-5: file_utils.py
위 4개 함수를 통합한 FileUtils 클래스

각 파일 하단에 테스트 코드 포함 (사용자 수정 가능한 테스트 변수 섹션 필수)
""")

Task(subagent_type="minimal-coder", prompt="""
INSTANCE_ID: 5
OUTPUT_DIR: spawn-test/output/instance-5/

## Main Task 5: JSON 유틸리티 모듈 구현

다음 5개의 sub-task를 순서대로 처리하세요.

### Sub-task 5-1: parse_json.py
JSON 문자열을 딕셔너리로 파싱하는 함수

### Sub-task 5-2: stringify_json.py
딕셔너리를 JSON 문자열로 변환하는 함수

### Sub-task 5-3: read_json.py
JSON 파일을 읽어 딕셔너리로 반환하는 함수

### Sub-task 5-4: write_json.py
딕셔너리를 JSON 파일로 저장하는 함수

### Sub-task 5-5: json_utils.py
위 4개 함수를 통합한 JsonUtils 클래스

각 파일 하단에 테스트 코드 포함 (사용자 수정 가능한 테스트 변수 섹션 필수)
""")
```

### 3단계: 결과 검증

모든 인스턴스 작업 완료 후 검증:

```
검증 체크리스트:
- [ ] 5개 인스턴스가 병렬로 spawn 되었는지
- [ ] 각 인스턴스가 5개의 sub-task를 처리했는지
- [ ] 총 25개 파일이 생성되었는지
- [ ] 각 파일에 테스트 코드가 포함되었는지
- [ ] minimal-coder 원칙 준수 (try/except 없음)

결과 요약:
- 병렬 spawn된 인스턴스 수: 5
- 인스턴스당 sub-task 수: 5
- 총 생성 파일 수: 25
```

---

## 핵심 포인트

### 병렬 실행 필수

5개의 Task() 호출이 반드시 하나의 메시지에서 동시에 이루어져야 합니다.

잘못된 방식:
```
메시지 1: Task(minimal-coder, "Main Task 1...")
메시지 2: Task(minimal-coder, "Main Task 2...")
메시지 3: Task(minimal-coder, "Main Task 3...")
```

올바른 방식:
```
[단일 메시지]:
  Task(minimal-coder, "Main Task 1...")
  Task(minimal-coder, "Main Task 2...")
  Task(minimal-coder, "Main Task 3...")
  Task(minimal-coder, "Main Task 4...")
  Task(minimal-coder, "Main Task 5...")
```

### 동일 에이전트 다중 인스턴스

- 에이전트 타입: minimal-coder (동일)
- 인스턴스 수: 5개 (각각 독립적인 context)
- 각 인스턴스의 작업: 서로 다른 도메인의 5개 sub-task

---

## 실행 지침

이 커맨드 실행 시:

1. 출력 디렉토리 생성
2. 5개의 minimal-coder 인스턴스를 단일 메시지에서 병렬 spawn
3. 각 인스턴스는 자신에게 할당된 5개 sub-task를 순차 처리
4. 모든 인스턴스 완료 후 결과 검증

지금 바로 실행하세요.
