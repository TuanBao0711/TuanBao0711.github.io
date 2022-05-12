<%-- 
    Document   : Left
    Created on : Apr 24, 2022, 10:40:39 PM
    Author     : b19dc
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<%@taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>

                <div class="col-sm-3">
                    <form action="category" method="post">
                        <div class="card bg-light mb-3">
                            <div class="card-header bg-primary text-white text-uppercase"><i class="fa fa-list"></i> Categories</div>
                            <div>
                                <c:forEach items="${listC}" var="o">
                                  <input name="category" type="radio" value="${o.cid}">&nbsp;&nbsp;&nbsp;${o.cname}<br/>
                                </c:forEach>
                            </div>
                        </div>
                        <div class="card bg-light mb-3">
                            <div>
                            <div class="card-header bg-primary text-white text-uppercase"><i class="fa fa-list"></i>Color</div>
<!--                            <div>Color</div>-->
<!--                            <div class="list-group category_block">-->
                               
<!--                                <input name="color" type="radio" class="list-group-item text-white" value="Đen"/>&nbsp; Đen 
                                <input name="color" type="radio" class="list-group-item text-white" value="Nâu"/>&nbsp; Nâu
                                
                                <input name="color" type="radio" class="list-group-item text-white" value="Trắng"/>&nbsp; Trắng-->
                                <div>
                                <input name="color" type="radio"  value="Đen"/>&nbsp;&nbsp;&nbsp;ĐEN <br/>
                               
                                <input name="color" type="radio"  value="Nâu"/>&nbsp;&nbsp;&nbsp;NÂU <br/>
                                
                                <input name="color" type="radio"  value="Trắng"/>&nbsp;&nbsp;&nbsp;TRẮNG <br/>
                                
                                </div>
                        </div>
                        </div>
                         <div class="card bg-light mb-3">
                            <div class="card-header bg-primary text-white text-uppercase"><i class="fa fa-list"></i>Price</div>
                            <div >
                                <input name="price" type="radio"  value="1"/>&nbsp;Dưới $200<br/>
                                <input name="price" type="radio"  value="2"/>&nbsp;Từ $200 đến $500<br/>
                                <input name="price" type="radio"  value="3"/>&nbsp;Trên $500<br/>
                            </div>
                        </div>
                        <input type="submit" value="Search"/>
                    </form>
                    
<!--                    <h2>${message}</h2>-->
                                  <br/>
                    <div class="card bg-light mb-3">
                        <div class="card-header bg-success text-white text-uppercase">New product</div>
                        <div class="card-body">
                            <img class="img-fluid" src="${p.image}" />
                            <h5 class="card-title">${p.name}</h5>
                            <p class="card-text">${p.title}</p>
                            <p class="bloc_left_price">$${p.price}</p>
                        </div>
                    </div>
                </div>
                        
 