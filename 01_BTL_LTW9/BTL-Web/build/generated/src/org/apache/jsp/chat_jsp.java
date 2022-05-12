package org.apache.jsp;

import javax.servlet.*;
import javax.servlet.http.*;
import javax.servlet.jsp.*;

public final class chat_jsp extends org.apache.jasper.runtime.HttpJspBase
    implements org.apache.jasper.runtime.JspSourceDependent {

  private static final JspFactory _jspxFactory = JspFactory.getDefaultFactory();

  private static java.util.List<String> _jspx_dependants;

  private org.glassfish.jsp.api.ResourceInjector _jspx_resourceInjector;

  public java.util.List<String> getDependants() {
    return _jspx_dependants;
  }

  public void _jspService(HttpServletRequest request, HttpServletResponse response)
        throws java.io.IOException, ServletException {

    PageContext pageContext = null;
    HttpSession session = null;
    ServletContext application = null;
    ServletConfig config = null;
    JspWriter out = null;
    Object page = this;
    JspWriter _jspx_out = null;
    PageContext _jspx_page_context = null;

    try {
      response.setContentType("text/html;charset=UTF-8");
      pageContext = _jspxFactory.getPageContext(this, request, response,
      			null, true, 8192, true);
      _jspx_page_context = pageContext;
      application = pageContext.getServletContext();
      config = pageContext.getServletConfig();
      session = pageContext.getSession();
      out = pageContext.getOut();
      _jspx_out = out;
      _jspx_resourceInjector = (org.glassfish.jsp.api.ResourceInjector) application.getAttribute("com.sun.appserv.jsp.resource.injector");

      out.write("\n");
      out.write("\n");
      out.write("\n");
      out.write("<!DOCTYPE html>\n");
      out.write("<html lang=\"en\">\n");
      out.write("\n");
      out.write("<head>\n");
      out.write("    <meta charset=\"UTF-8\">\n");
      out.write("    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n");
      out.write("    <title>Advanced Level Chat-Box UI</title>\n");
      out.write("    <link rel=\"stylesheet\" href=\"css/stylec.css\">\n");
      out.write("</head>\n");
      out.write("\n");
      out.write("<body>\n");
      out.write("\n");
      out.write("    <div class=\"container_chat\">\n");
      out.write("        <!-- chat box -->\n");
      out.write("        <div class=\"chat-box\">\n");
      out.write("            <!-- client -->\n");
      out.write("            <div class=\"client\">\n");
      out.write("                <img src=\"images/logo/icon.png\" alt=\"logo\" />\n");
      out.write("                <div class=\"client-info\">\n");
      out.write("                    <h2>BBH shop</h2>\n");
      out.write("                    <p>online</p>\n");
      out.write("                </div>\n");
      out.write("            </div>\n");
      out.write("\n");
      out.write("            <!-- main chat section -->\n");
      out.write("            <div class=\"chats\">\n");
      out.write("                <div class=\"client-chat\">Xin chào!</div>\n");
      out.write("                <div class=\"admin-chat\">Xin chào, shop có thể giúp gì cho bạn?</div>\n");
      out.write("<!--                <div class=\"client-chat\">How can i help you?</div>\n");
      out.write("                <div class=\"my-chat\">How you create this chat box?</div>\n");
      out.write("                <div class=\"client-chat\">Watch complete video for your answer.</div>-->\n");
      out.write("            </div>\n");
      out.write("\n");
      out.write("            <!-- input field section -->\n");
      out.write("            <div class=\"chat-input\">\n");
      out.write("                <input name=\"chat_input\" type=\"text\" placeholder=\"Enter Message\" />\n");
      out.write("                <button class=\"send-btn\">\n");
      out.write("                    <a href=\"chat\"><img src=\"images/chat/send.png\" alt=\"send-btn\"></a>\n");
      out.write("                </button>\n");
      out.write("            </div>\n");
      out.write("        </div>\n");
      out.write("\n");
      out.write("        <!-- button -->\n");
      out.write("        <div class=\"chat-btn\">\n");
      out.write("            <img src=\"images/chat/Circle-icons-chat.svg.png\" alt=\"chat box icon btn\">\n");
      out.write("        </div>\n");
      out.write("    </div>\n");
      out.write("\n");
      out.write("    <script src=\"js/jquery-3.4.1.min.js\"></script>\n");
      out.write("    <script src=\"js/script.js\"></script>\n");
      out.write("</body>\n");
      out.write("\n");
      out.write("</html>\n");
    } catch (Throwable t) {
      if (!(t instanceof SkipPageException)){
        out = _jspx_out;
        if (out != null && out.getBufferSize() != 0)
          out.clearBuffer();
        if (_jspx_page_context != null) _jspx_page_context.handlePageException(t);
        else throw new ServletException(t);
      }
    } finally {
      _jspxFactory.releasePageContext(_jspx_page_context);
    }
  }
}
