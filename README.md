# UsingChatGPT

* Poetry 가상환경 활성화 순서

1) 현재 Poetry 프로젝트에서 사용 중인 **가상환경(virtual environment)**의 경로 출력 확인
   poetry env info --path

   결과 예시) c:\dev\1-6-llm\.venv


2) PowerShell을 "관리자 권한"으로 실행 후 아래 명령 실행 (로컬에서 만든 스크립트는 서명 없이 실행 가능하게 함)

     Set-ExecutionPolicy RemoteSigned -Scope CurrentUser

![image](https://github.com/user-attachments/assets/b6f3684c-d307-4f0d-b4fc-d27ad04d6c1d)


3) PowerShell에서 가상환경 진입 명령어

   & "c:\dev\1-6-llm\.venv\Scripts\Activate.ps1"
   
![image](https://github.com/user-attachments/assets/494c7eb7-aeba-4114-b9e7-5dc999b8735f)



4) (필요시)모듈, 패키지 추가
   
     poetry add fastapi
  
     poetry add uvicorn

