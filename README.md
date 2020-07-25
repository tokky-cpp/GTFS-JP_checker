# GTFS-JP_checker
[開発中] GTFS-JP形式に則ったデータであるか判定し、そうでない場合は相違のある箇所を提示するツール

# 開発経緯
GTFSのオープンソースのチェックツールとして[FeedValidator](https://github.com/google/transitfeed/wiki/FeedValidator)が存在しますが、GTFS-JPのオープンソースのチェックツールが見当たらない（もしあれば連絡いただけますと助かります）ため、開発を開始しました。

# 開発方針
本リポジトリはgithub flowで開発することを目指します（強制するものではありません）。
どなたでも開発に参加いただけます（参加いただけると助かります）。

# GTFS-JPについて
バスをはじめとした交通機関の運行に関する情報を経路探索システムで扱うための共通フォーマットです。
詳しくは[こちら](https://www.gtfs.jp/)をご覧ください。

# 各フォルダ／ファイルの説明
- src/ : プログラムを保存するフォルダ
- config.txt : 設定記述（チェックするGTFSデータの保存場所など）
- run.sh : チェックツールの一括実行シェルスクリプト

## TODO(中長期的)
- 必要ファイル群があることをチェック
- ファイル内において必須カラムがあることをチェック
- ローカルweb上でチェックできるようにする
