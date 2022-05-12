    <%-- 
    Document   : Menu
    Created on : Apr 24, 2022, 10:31:02 PM
    Author     : b19dc
--%>

<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@page contentType="text/html" pageEncoding="UTF-8"%>

<!--begin of menu-->
        <nav class="navbar navbar-expand-md navbar-dark bg-dark">
            <div class="container">
                <a class="navbar-brand" href="product"><img src="images/logo/4.png" alt="logo images"></a>
                <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarsExampleDefault" aria-controls="navbarsExampleDefault" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>

                <div class="collapse navbar-collapse justify-content-end" id="navbarsExampleDefault">
                    <ul class="navbar-nav m-auto">
                        
                        <c:if test="${sessionScope.acc.isAdmin == 1}">
                            <li class="nav-item">
                                <a class="nav-link" href="#">Quản lý tài khoản</a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link" href="https://www.facebook.com/messages/t/105707792139396">Chat với chúng tôi</a>
                            </li>
                        </c:if>
                        
                         <c:if test="${sessionScope.acc.isSell == 1}">
                            <li class="nav-item">
                                <a class="nav-link" href="manager">Quản lý sản phẩm</a>
                            </li>
                         </c:if>
                        
                        <c:if test="${sessionScope.acc!=null}">
                            <li class="nav-item">
                                <a class="nav-link" href="history">Xin chào ${sessionScope.acc.name}</a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link" href="logout">Đăng xuất</a>
                            </li>
                             <li class="nav-item">
                                <a class="nav-link" href="https://www.facebook.com/messages/t/105707792139396">Chat với chúng tôi</a>
                            </li>
                        </c:if>
                        <c:if test="${sessionScope.acc==null}">
                            <li class="nav-item">
                                <a class="nav-link" href="Login.jsp">Đăng nhập</a>
                            </li>
                         </c:if>
                    </ul>

                    <form action="search" method="post" class="form-inline my-2 my-lg-0">
                        <div class="input-group input-group-sm">
                            <input value="${txts}" name="txt" type="text" class="form-control" aria-label="Small" aria-describedby="inputGroup-sizing-sm" placeholder="Search...">
                            <div class="input-group-append">
                                <button type="submit" class="btn btn-secondary btn-number">
                                    <i class="fa fa-search"></i>
                                </button>
                            </div>
                        </div>
                        <a class="btn btn-success btn-sm ml-3" href="show">
                            <i class="fa fa-shopping-cart"></i> Giỏ hàng
                            <span class="badge badge-light">${requestScope.size}</span>
                        </a>
                    </form>
                </div>
            </div>
        </nav>
        <section class="jumbotron text-center">
            <div class="container">
                <div style="background-image: url(images/bg/big_pic.jpg); height: 250px">
<!--                    <h1 class="jumbotron-heading">Nội thất cao cấp</h1>-->
<!--                    <p class="lead text-muted mb-0" > <b>Uy tín tạo nên thương hiệu với hơn 10 năm cung cấp các sản phẩm nội thất</b></p>-->
                </div>
                
<!--                <div ><img src="images/bg/big_pic.jpg" alt="logo images"></div>-->
<!--                <div class="ht__bradcaump__area" style="background: rgba(0, 0, 0, 0) url(images/bg/big_pic.jpg) no-repeat scroll center center / cover ;">-->
                     
            </div>
        </section>
        <!--end of menu-->
