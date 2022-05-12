<%-- 
    Document   : mycart
    Created on : Apr 27, 2022, 10:56:56 AM
    Author     : b19dc
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<%@taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@taglib prefix="fmt" uri="http://java.sun.com/jsp/jstl/fmt"%>

<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>web ban hang</title>
        <style>
            table{
                border-collapse: collapse;
            }
            .tr{
                text-align: right;
            }
            a{
                text-decoration: none;
                color: chocolate;
                font-size: 22px;
                font-weight: bold;
            }
        </style>
    </head>
    <body>
        <h1>Shopping Cart Online</h1>
        <table border="1px" width="40%">
            <tr>
                <th>No</th>
                <th>Name</th>
                <th>Quantity</th>
                <th>Price</th>
                <th>Total Money</th>
            </tr>
            <c:set var="o" value="${requestScope.cart}"/>
            <c:set var="tt" value="0"/>
            <c:forEach items="${o.items}" var="i">
                <c:set var="tt" value="${tt+1}"/>
                <tr>
                    <td>${tt}</td>
                    <td>${i.product.name}</td>
                    <td>
                        <button><a href="process?num=-1&id=${i.product.id}">-</a></button>
                        ${i.quantity}
                        <button><a href="process?num=1&id=${i.product.id}">+</a></button>
                    </td>
                    <td class="tr">
                       ${i.price}
                    </td>
                    <td class="tr">
                       ${ i.price*i.quantity}
                    </td>
                    <td style="text-align: center">
                        <form action="process" method="post">
                            <input type="hidden" name="id" value="${i.product.id}"/>
                            <input type="submit" value="Return Item"/>
                        </form>
                    </td>
                </tr>
            </c:forEach>
        </table>
            <h3>Total Money: $ ${o.totalMoney}</h3>
            <form action="checkout" method="post">
                <input type="submit" value="Check out"/>
            </form>
            <hr/>
            <a href="product">CLICK ME TO CONTINUE SHOPPINGgggg</a>
    </body>
</html>
