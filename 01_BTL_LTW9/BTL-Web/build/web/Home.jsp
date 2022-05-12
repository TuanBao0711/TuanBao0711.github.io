<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>Nội thất trang trí cao cấp</title>
        <link href="//maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" rel="stylesheet" id="bootstrap-css">
        <script src="//maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"></script>
        <script src="//cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
        <!------ Include the above in your HEAD tag ---------->
        <link href="https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet" integrity="sha384-wvfXpqpZZVQGK6TAh5PVlGOfQNHSoD2xbE+QkPxCAFlNEevoEH3Sl0sibVcOQVnN" crossorigin="anonymous">
        <link href="css/style.css" rel="stylesheet" type="text/css"/>
    </head>
    <body>

        <jsp:include page="Menu.jsp"></jsp:include>
        <div class="container">
            <div class="row">
                <div class="col">
                    <nav aria-label="breadcrumb">
                        <ol class="breadcrumb">
                            <li class="breadcrumb-item"><a href="product">Home</a></li>
                            <li class="breadcrumb-item"><a href="category">Category</a></li>
                        
                        </ol>
                    </nav>
                </div>
            </div>
        </div>
        <div class="container">
            <div class="row">
            <jsp:include page="Left.jsp"></jsp:include>

                <div class="col-sm-9">
                    <div class="row">
                        <c:forEach items="${listP}" var="o">
                            <div class="col-12 col-md-6 col-lg-4">
                                <div class="card"> 
                                    <img class="card-img-top" src="${o.image}" alt="Card image cap">
                                    <div class="card-body">
                                        <h4 class="card-title show_txt"><a href="detail?pid=${o.id}" title="View Product">${o.name}</a></h4>
                                        <p class="card-text show_txt">${o.title}</p>
                                        <div class="row">
                                            <div class="col">
                                                <p class="btn btn-danger btn-block">$${o.price}</p>    
                                               
                                            </div>
                                            <c:if test="${o.quantity == 0}">
                                                <div style="color:blue" class="col">
                                                    <p class="btn btn-danger btn-block">Hết hàng</p>    
                                                </div> 
                                            </c:if>
                                                
                                            <c:if test="${o.quantity > 0}">
                                                <div class="col">
                                                    <p class="btn btn-danger btn-block">${o.quantity}</p>    
                                                </div> 
                                            </c:if>
                                            <div class="col">
                                                <a href="buy?id=${o.id}" class="btn btn-success btn-block">Add to cart</a>
                                                <!--<input class="btn btn-success btn-block" type="button" onclick="buy('${o.id}')" value="Add to Cart"/>-->
                                            </div>
                                             
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </c:forEach>
                    </div>
                </div>

            </div>
        </div>
     <jsp:include page="Footer.jsp"></jsp:include>
     
    </body>
</html>
<script type="text/javascript">
    function buy(id){
        var m = document.f.num.value;
        document.f.action="buy?id="+id+"&num="+m;
        document.f.submit();
    }
</script>

