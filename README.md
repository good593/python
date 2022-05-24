# python

## github repository로 python pip install 만들기
- https://lsjsj92.tistory.com/592
- https://ihopeido.tistory.com/entry/python-eggs-%EA%B0%84%EB%8B%A8%ED%95%9C-%EC%86%8C%EA%B0%9C
### setuup.py
> pip install을 할 때 사용되는 python package setup 정보입니다. name, description, version 등이 여기에 포함되어 있습니다.  
```python
from setuptools import setup

setup(
  name='common_lib',
  version='0.0.1',
  description='pip install test',
  url="https://git-codecommit.ap-northeast-2.amazonaws.com/v1/repos/pip-install-base",
  author='&&&&',
  author_email='&&&&@gmail.com',
  license='$$$$',
  packages=['common_lib'],
  zip_safe=False,
  install_requires=[
    'numpy==1.18.3'
  ]
)
```

