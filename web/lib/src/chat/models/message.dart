class Message {

  int id;

  String message;
  String messageType;
  String createdAt;

  dynamic data;

  Message({this.id, this.message, this.messageType, this.data, this.createdAt});

  factory Message.fromJson(Map<String, dynamic> json){
    var res = Message(
      id: json['id'],
      message: json['message'],
      messageType: json['messageType'],
      createdAt: json['createdAt'],
      data: json['data']
    );

    return res;
  }

}