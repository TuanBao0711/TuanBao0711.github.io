<%-- 
    Document   : Login
    Created on : Apr 20, 2022, 10:16:37 PM
    Author     : b19dc
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<link href="//maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" rel="stylesheet" id="bootstrap-css">
<script src="//maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"></script>
<script src="//cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
<!------ Include the above in your HEAD tag ---------->

<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Ðang Nhap</title>
        <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto|Varela+Round">
        <link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css">
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
        <link href="css/manager.css" rel="stylesheet" type="text/css"/>
        <style>
          .gradient-custom-2 {
            /* fallback for old browsers */
            background: #fccb90;

            /* Chrome 10-25, Safari 5.1-6 */
            background: -webkit-linear-gradient(to right, #ee7724, #d8363a, #dd3675, #b44593);

            /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */
            background: linear-gradient(to right, #ee7724, #d8363a, #dd3675, #b44593);
            }

            @media (min-width: 768px) {
            .gradient-form {
            height: 100vh !important;
            }
            }
            @media (min-width: 769px) {
            .gradient-custom-2 {
            border-top-right-radius: .3rem;
            border-bottom-right-radius: .3rem;
            }
            }
        </style>
    </head>
    <body>
        <<section class="h-100 gradient-form" style="background-color: #eee;">
  <div class="container py-5 h-100">
    <div class="row d-flex justify-content-center align-items-center h-100">
      <div class="col-xl-10">
        <div class="card rounded-3 text-black">
          <div class="row g-0">
            <div class="col-lg-6">
              <div class="card-body p-md-5 mx-md-4">

                <div class="text-center">
                  <img src="images/logo/4.png"
                    style="width: 185px;" alt="logo">
                  
                  <h4 class="mt-1 mb-5 pb-1"  style="margin-top: 100px ">Luôn hết mình phục vụ khách hàng </h4>
                </div>

                <form action="login" method="post">
                  <p>Vui lòng đăng nhập</p>
                  
                  <div class="form-outline mb-4">
                    <input name="user" type="text" id="form2Example11" class="form-control"
                      placeholder="UserName" />
                    <label class="form-label" for="form2Example11">Tên tài khoản</label>
                  </div>

                  <div class="form-outline mb-4">
                    <input name="pass" type="password" id="form2Example22" class="form-control"
                           placeholder="Password"/>
                    <label class="form-label" for="form2Example22">Mật khẩu</label>
                  </div>

<!--                  <div class="text-center pt-1 mb-5 pb-1">
                    <button class="btn btn-primary btn-block fa-lg gradient-custom-2 mb-3" type="button">Log
                      in</button>
                    <a class="text-muted" href="#!">Forgot password?</a>
                  </div>

                  <div class="d-flex align-items-center justify-content-center pb-4">
                    <p class="mb-0 me-2">Don't have an account?</p>
                    <button type="button" class="btn btn-outline-danger">Create new</button>
                  </div>-->
                  <input type="submit" class="btn btn-primary btn-block fa-lg gradient-custom-2 mb-3" value="Login"/>
                    
                </form>
<!--                <div class="text-center pt-1 mb-5 pb-1">
                     <button class="btn btn-primary btn-block fa-lg gradient-custom-2 mb-3" type="button">Log
                      in</button>
                    <a class="text-muted" href="#!">Forgot password?</a>
                  </div>-->
                    <p class="text-danger">
                    ${message}
                    </p>
                  <div class="d-flex align-items-center justify-content-center pb-4">
                    <p class="mb-0 me-2">Bạn chưa có tài khoản?</p>
                    <button type="button" class="btn btn-outline-danger"><a href="Registered.jsp">Đăng ký</a></button>
                  </div>

              </div>
            </div>
            <div class="col-lg-6 d-flex align-items-center gradient-custom-2">
              <div class="text-white px-3 py-4 p-md-5 mx-md-4">
                  <img src="images/blog/blog-img/blog1.png" style="width: 350px; height: 300px" alt="blog images">
<!--                <h4 class="mb-4">We are more than just a company</h4>
                <p class="small mb-0">Bản thân nỗi đau là quan trọng, nhưng nỗi đau được tăng cường bởi quá trình tạo mỡ, nhưng tôi cho nó thời gian để cắt giảm nó để tôi làm một số công việc lớn và nỗi đau. Để phần lớn điều đó xảy ra, bất kỳ ai trong chúng ta cũng sẽ thực hiện bất kỳ loại công việc nào ngoại trừ để tận dụng các mục tiêu từ nó.</p>-->
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
    </body>
</html>