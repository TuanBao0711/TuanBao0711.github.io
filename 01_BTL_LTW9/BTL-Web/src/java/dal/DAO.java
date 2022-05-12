/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package dal;

import com.oracle.webservices.internal.api.databinding.DatabindingModeFeature;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;
import model.Account;
import model.Cart;
import model.Category;
import model.Item;
import model.Order;
import model.Product;

/**
 *
 * @author b19dc
 */
public class DAO extends DBContext{
  
    public List<Product> getAllProducts(){
       List<Product> list = new ArrayList<>();
       String sql = "select *from Product where [title] is not null";
       try{
         PreparedStatement st  = connection.prepareStatement(sql);
         ResultSet rs = st.executeQuery();
         while (rs.next()){
            list.add(new Product(rs.getInt("id"),
                                rs.getString("name"),
                                rs.getString("image"),
                                rs.getDouble("price"),
                                rs.getString("title"),
                                rs.getString("description"),
                                rs.getInt("quantity")));
         }
       }catch(SQLException e){
           System.out.println(e);
       }
       return list;
    } 
    
    public void setTitle(int id){
        String sql = "update Product set title=null where id=?";
        try {
            PreparedStatement st = connection.prepareStatement(sql);
            st.setInt(1, id);
            st.executeUpdate();
        } catch (SQLException e) {
            System.out.println(e);
        }
        
    }
    
    public void setHien(int id){
        String sql = "update Product set title=N'Đen' where id=?";
        try {
            PreparedStatement st = connection.prepareStatement(sql);
            st.setInt(1, id);
            st.executeUpdate();
        } catch (SQLException e) {
            System.out.println(e);
        }
        
    }
    
    public List<Product> getProductByCategory(String cid){
         List<Product> list = new ArrayList<>();
       String sql = "select *from Product where cateID=?";
       try{
         PreparedStatement st  = connection.prepareStatement(sql);
         st.setString(1, cid);
         ResultSet rs = st.executeQuery();
         while (rs.next()){
            list.add(new Product(rs.getInt("id"),
                                rs.getString("name"),
                                rs.getString("image"),
                                rs.getDouble("price"),
                                rs.getString("title"),
                                rs.getString("description"),
                                rs.getInt("quantity")));
         }
       }catch(SQLException e){
           System.out.println(e);
       }
       return list;
    }
    
    public Product getProductById(int id){
       String sql = "select *from Product where id=?";
       try{
         PreparedStatement st  = connection.prepareStatement(sql);
         st.setInt(1, id);
         ResultSet rs = st.executeQuery();
         if (rs.next()){
            return new Product(rs.getInt("id"),
                                rs.getString("name"),
                                rs.getString("image"),
                                rs.getDouble("price"),
                                rs.getString("title"),
                                rs.getString("description"),
                                rs.getInt("quantity"));
         }
       }catch(SQLException e){
           System.out.println(e);
       }
       return null;
    }
    
    public List<Product> getProductBySellId(int id){
       List<Product> list  = new ArrayList<>();
       String sql = "select *from Product where sell_ID=?";
       try{
         PreparedStatement st  = connection.prepareStatement(sql);
         st.setInt(1, id);
         ResultSet rs = st.executeQuery();
         while (rs.next()){
            list.add(new Product(rs.getInt("id"),
                                rs.getString("name"),
                                rs.getString("image"),
                                rs.getDouble("price"),
                                rs.getString("title"),
                                rs.getString("description"),
                                rs.getInt("quantity")));
         }
       }catch(SQLException e){
           System.out.println(e);
       }
       return list;
    }
    
    public void insert(String name,String user,String pass,int x){
        List<Account> list = new ArrayList<>();
        String sql = "select *from Customer";
        try{
          PreparedStatement st  = connection.prepareStatement(sql);
          ResultSet rs = st.executeQuery();
          while (rs.next()){
             list.add(new Account (rs.getInt("id"),
                                rs.getString("name"),
                                rs.getDouble("amount"),
                                user,
                                pass,
                                rs.getInt("isSell"),
                                rs.getInt("isAdmin")));
          }
        }catch(SQLException e){
            System.out.println(e);
        }
        int id = list.get(list.size()-1).getId()+1;
        String sql1 = "insert into customer values(?,?,0,?,?,?,0)";
        try {
            PreparedStatement st1  = connection.prepareStatement(sql1);
            st1.setInt(1,id);
            st1.setString(2, name);
            st1.setString(3,user);
            st1.setString(4, pass);
            st1.setInt(5, x);
            st1.executeUpdate();
        } catch (SQLException e) {
            System.out.println(e);
        }
    }
    
    public Account check(String user,String pass){
       String sql = "select *from customer where [username]  = ? and password=?";
       try{
         PreparedStatement st  = connection.prepareStatement(sql);
         st.setString(1,user);
         st.setString(2,pass);
         ResultSet rs = st.executeQuery();
         while (rs.next()){
            return new Account (rs.getInt("id"),
                                rs.getString("name"),
                                rs.getDouble("amount"),
                                user,
                                pass,
                                rs.getInt("isSell"),
                                rs.getInt("isAdmin"));
         }
       }catch(SQLException e){
           System.out.println(e);
       }
       return null;
    } 
    
    public Account checkAccountExit(String user){
       String sql = "select *from customer where [username]  = ? ";
       try{
         PreparedStatement st  = connection.prepareStatement(sql);
         st.setString(1,user);
         ResultSet rs = st.executeQuery();
         while (rs.next()){
            return new Account (rs.getInt("id"),
                                rs.getString("name"),
                                rs.getDouble("amount"),
                                user,
                                rs.getString("password"),
                                rs.getInt("isSell"),
                                rs.getInt("isAdmin"));
         }
       }catch(SQLException e){
           System.out.println(e);
       }
       return null;
    } 
    
    public Product getProductByID(String id){
       String sql = "select *from product where id=?";
       try{
         PreparedStatement st  = connection.prepareStatement(sql);
         st.setString(1, id);
         ResultSet rs = st.executeQuery();
         while (rs.next()){
            return new Product(rs.getInt("id"),
                                rs.getString("name"),
                                rs.getString("image"),
                                rs.getDouble("price"),
                                rs.getString("title"),
                                rs.getString("description"),
                                rs.getInt("quantity"));
         }
       }catch(SQLException e){
           System.out.println(e);
       }
       return null;
    } 
    
    public List<Product> searchByName(String txtSearch){
       List<Product> list = new ArrayList<>();
       String sql = "select *from product where [name] like ?";
       try{
         PreparedStatement st  = connection.prepareStatement(sql);
         st.setString(1,"%"+  txtSearch + "%");
         ResultSet rs = st.executeQuery();
         while (rs.next()){
            list.add(new Product(rs.getInt("id"),
                                rs.getString("name"),
                                rs.getString("image"),
                                rs.getDouble("price"),
                                rs.getString("title"),
                                rs.getString("description"),
                                rs.getInt("quantity")));
         }
       }catch(SQLException e){
           System.out.println(e);
       }
       return list;
    } 
    
    
    public List<Category> getAllCategories(){
       List<Category> list = new ArrayList<>();
       String sql = "select *from Category";
       try{
         PreparedStatement st  = connection.prepareStatement(sql);
         ResultSet rs = st.executeQuery();
         while (rs.next()){
            list.add(new Category(rs.getInt(1),
                                rs.getString(2)
                                ));
         }
       }catch(SQLException e){
           System.out.println(e);
       }
       return list;
    }
    
    public Product getLast(){
        String sql = "select top 1 *from product order by id desc";
        try {
            PreparedStatement st  = connection.prepareStatement(sql);
            ResultSet rs = st.executeQuery();
            while (rs.next()){
                return new Product(rs.getInt("id"),
                                rs.getString("name"),
                                rs.getString("image"),
                                rs.getDouble("price"),
                                rs.getString("title"),
                                rs.getString("description"),
                                rs.getInt("quantity"));
            }
        } catch (SQLException e) {
            System.out.println(e);
        }
        return null;
    }
    
    public void deleteProduct(String pid){
        String sql = "delete from product where id=?";
        try {
            PreparedStatement st  = connection.prepareStatement(sql);
            st.setString(1, pid);
            st.executeUpdate();
        } catch (SQLException e) {
            System.out.println(e);
        }
    }
    
    public void insertProduct(int id,String name,String price,String quantity,
            String desc, String category,String title,String image,int sid){
        String sql = "insert[dbo].[product] ([id], [name], [price], [quantity], [description], "
                + "[cateID], [title], [image],[sell_ID]) VALUES(?,?,?,?,?,?,?,?,?)";
        try {
            PreparedStatement st  = connection.prepareStatement(sql);
            st.setInt(1, id);
            st.setString(2, name);
            st.setString(8, image);
            st.setString(3, price);    
            st.setInt(4, Integer.parseInt(quantity));
            st.setString(7, title);
            st.setString(5, desc);
            st.setString(6, category);
            st.setInt(9, sid);
            st.executeUpdate();
        } catch (SQLException e) {
            System.out.println(e);
        }
    }
    
    public void editProduct(int id,String name,String price,String quantity,
            String desc, String category,String title,String image){
        String sql ="update product set [name] = ?,[image] = ?,[price]=?,\n" +
                    " [title]=?,[description]= ?,cateID = ?,quantity = ? where id=?";
        try {
            PreparedStatement st  = connection.prepareStatement(sql);
            st.setString(1,name);
            st.setString(2, image);
            st.setString(3, price);
            st.setString(4,title);
            st.setString(5,desc);
            st.setString(6, category);
            st.setInt(7, Integer.parseInt(quantity));
            st.setInt(8, id);
            st.executeUpdate();
        } catch (SQLException e) {
            System.out.println(e);
        }
    }
    
    public List<Order> getOrderByCid(int cid){
        List<Order> list = new ArrayList<>();
        String sql = "select *from [Order] where cid=?";
        try {
            PreparedStatement st = connection.prepareStatement(sql);
            st.setInt(1, cid);
            ResultSet rs = st.executeQuery();
            while (rs.next()){
                list.add(new Order(rs.getInt("id"),
                                   rs.getString("date"),
                                   rs.getInt("cid"),
                                   rs.getDouble("totalmoney")));
            }
        } catch (SQLException e) {
        }
        return list;
    }
    
    public void addOrder(Account c, Cart cart){
        LocalDate curDate  = LocalDate.now();
        String date = curDate.toString();
        try {
            // add order
            String sql = "insert into [order] values(?,?,?)";
            PreparedStatement st = connection.prepareStatement(sql);
            st.setString(1,date);
            st.setInt(2, c.getId());
            st.setDouble(3, cart.getTotalMoney());
            st.executeUpdate();
            
            // Lay id cua order vua add
            String sql1 = "select top 1 id from [order] order by id desc";
            PreparedStatement st1 = connection.prepareStatement(sql1);
            ResultSet rs = st1.executeQuery();
            
            // add vao bang orderdetail
            if (rs.next()){
                int oid = rs.getInt("id");
                for (Item i:cart.getItems()){
                    String sql2 = "insert into [orderline] values(?,?,?,?)";
                    PreparedStatement st2 = connection.prepareStatement(sql2);
                    st2.setInt(1, oid);
                    st2.setInt(2, i.getProduct().getId());
                    st2.setInt(3, i.getQuantity());
                    st2.setDouble(4,i.getPrice());  
                    st2.executeUpdate();
                }
            }
            
            // cap nhat lai so luong 
            String sql3 = "update product set quantity=quantity-? where id=?";
            PreparedStatement st3 = connection.prepareStatement(sql3);
            for (Item i:cart.getItems()){
                st3.setInt(1, i.getQuantity());
                st3.setInt(2, i.getProduct().getId());
                st3.executeUpdate();
            }
        } catch (SQLException e) {
        }
    }
    
    public List<Product> getProductByFilter(String cid,String color, String price){
       List<Product> list = new ArrayList<>();    
       String sql = "Select *from Product where "+ cid + color + price;
       try{
         PreparedStatement st  = connection.prepareStatement(sql);
         ResultSet rs = st.executeQuery();
         while (rs.next()){
            list.add(new Product(rs.getInt("id"),
                                rs.getString("name"),
                                rs.getString("image"),
                                rs.getDouble("price"),
                                rs.getString("title"),
                                rs.getString("description"),
                                rs.getInt("quantity")));
         }
       }catch(SQLException e){
           System.out.println(e);
       }
       return list;
    } 
    
    public static void main(String[] args) {
        DAO c = new DAO();
       
        List<Product> list = c.getProductByFilter(null, "Nâu", "1");
        for (Product x:list){
            String hd = x.getId()+" "+x.getName();
            System.out.println(hd);
        }
    }
}
