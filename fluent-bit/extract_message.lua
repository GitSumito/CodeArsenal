function extract_fields(tag, timestamp, record)
    local message = record["message"]
    if message ~= nil and type(message) == "string" then
        -- トランザクションIDの抽出
        local transaction_id = message:match('"transaction_id":"(.-)"')
        record["transaction_id"] = transaction_id

        -- ログインIDの抽出
        local login_id = message:match('"login_id":(%d+)')
        record["login_id"] = login_id

        -- パスの抽出
        local path = message:match('"path":"(.-)"')
        record["path"] = path

        -- メソッドの抽出
        local method = message:match('"method":"(.-)"')
        record["method"] = method

        -- ログタイプの抽出
        local log_type = message:match('"log_type":"(.-)"')
        record["log_type"] = log_type

        -- 通知の抽出
        local notification = message:match('"notification":(%d+)')
        record["notification"] = notification

        -- リクエストパラメータの抽出
        local request_params = message:match('"request_params":({.-})')
        record["request_params"] = request_params
    end
    return 1, timestamp, record
end
