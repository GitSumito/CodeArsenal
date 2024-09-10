from locust import HttpUser, task, between
import re

class WebAppUser(HttpUser):
    # リクエスト間の待機時間を1〜3秒にランダム設定
    wait_time = between(1, 3)
    
    def on_start(self):
        # テスト開始時にログインを実行
        self.login()

    def login(self):
        login_url = "/login"
        
        # ログインページにアクセス
        response = self.client.get(login_url)
        
        # CSRFトークンを取得
        # 正規表現を使用してHTMLからCSRFトークンを抽出
        # 1. re.search()関数:
        #    - 第一引数: 検索パターン（正規表現）
        #    - 第二引数: 検索対象の文字列（ここではHTMLの内容）
        #
        # 2. 正規表現 'name="_token" value="(.+?)"':
        #    - name="_token" value=": この文字列を含む部分を探す
        #    - (.+?): 括弧内の.+?は、任意の文字（.）が1回以上（+）、
        #             ただし最小の範囲で（?）マッチすることを意味する
        #    - この正規表現は、<input name="_token" value="xxxxxxxx"> のような
        #      HTMLタグからトークン値を抽出することを目的としている
        #
        # 3. if csrf_token:
        #    - re.search()がマッチを見つけた場合、結果オブジェクトが返される
        #    - マッチが見つからなかった場合はNoneが返される
        #
        # 4. csrf_token.group(1):
        #    - group(1)は、正規表現の最初の括弧（）でキャプチャされた部分を返す
        #    - これにより、実際のトークン値のみを取得できる
        #
        # 5. else節:
        #    - CSRFトークンが見つからない場合、セキュリティ上の問題や
        #      HTMLの構造変更の可能性があるため、エラーメッセージを表示し処理を中断する
        csrf_token = re.search('name="_token" value="(.+?)"', response.text)
        if csrf_token:
            csrf_token = csrf_token.group(1)
        else:
            print("CSRF token not found")
            return

        # ログインフォームのデータを準備
        login_data = {
            "email": "your_email@example.com",
            "password": "your_password",
            "_token": csrf_token
        }
        
        # ヘッダーを設定（フォームデータを送信することを指定）
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        
        # ログインリクエストを送信
        response = self.client.post(login_url, data=login_data, headers=headers)
        
        # ログイン成功の確認
        # ログイン後のリダイレクト先URLに'dashboard'が含まれているか確認
        if "dashboard" in response.url:
            print("Login successful")
        else:
            print("Login failed")

    @task
    def access_specific_page(self):
        # テストで確認したい特定のページのURL
        specific_url = "/specific/page"
        
        # 特定のページにGETリクエストを送信
        response = self.client.get(specific_url)
        
        # レスポンスのステータスコードを確認
        if response.status_code == 200:
            print(f"Successfully accessed page: {response.url}")
        else:
            print(f"Failed to access page. Status code: {response.status_code}")

class WebsiteUser(HttpUser):
    # WebAppUserクラスをタスクとして設定
    tasks = [WebAppUser]
    
    # テスト対象のWebサイトのベースURL
    host = "https://your-website.com"
