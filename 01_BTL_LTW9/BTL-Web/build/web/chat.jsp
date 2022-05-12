<%-- 
    Document   : chat
    Created on : May 9, 2022, 3:02:47 PM
    Author     : Admin
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Advanced Level Chat-Box UI</title>
    <link rel="stylesheet" href="css/stylec.css">
</head>

<body>

    <div class="container_chat">
        <!-- chat box -->
        <div class="chat-box">
            <!-- client -->
            <div class="client">
                <img src="images/logo/icon.png" alt="logo" />
                <div class="client-info">
                    <h2>BBH shop</h2>
                    <p>online</p>
                </div>
            </div>

            <!-- main chat section -->
            <div class="chats">
                <div class="client-chat">Xin chào!</div>
                <div class="admin-chat">Xin chào, shop có thể giúp gì cho bạn?</div>
<!--                <div class="client-chat">How can i help you?</div>
                <div class="my-chat">How you create this chat box?</div>
                <div class="client-chat">Watch complete video for your answer.</div>-->
            </div>

            <!-- input field section -->
            <div class="chat-input">
                <input name="chat_input" type="text" placeholder="Enter Message" />
                <button class="send-btn">
                    <a href="chat"><img src="images/chat/send.png" alt="send-btn"></a>
                </button>
            </div>
        </div>

        <!-- button -->
        <div class="chat-btn">
            <img src="images/chat/Circle-icons-chat.svg.png" alt="chat box icon btn">
        </div>
    </div>

    <script src="js/jquery-3.4.1.min.js"></script>
    <script src="js/script.js"></script>
</body>

</html>
