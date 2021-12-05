package uz.fairUzbekistan;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import org.telegram.telegrambots.bots.TelegramLongPollingBot;
import org.telegram.telegrambots.meta.api.methods.send.SendLocation;
import org.telegram.telegrambots.meta.api.methods.send.SendMessage;
import org.telegram.telegrambots.meta.api.objects.Message;
import org.telegram.telegrambots.meta.api.objects.Update;
import org.telegram.telegrambots.meta.exceptions.TelegramApiException;
import uz.fairUzbekistan.helper.GsonUserHelper;
import uz.fairUzbekistan.model.Application;
import uz.fairUzbekistan.model.User;
import uz.fairUzbekistan.sender.ReplyKeyboardSender;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.io.Writer;
import java.util.ArrayList;
import java.util.List;
import java.util.Objects;

public class FairUzbekistan extends TelegramLongPollingBot {
    File userFile = new File("src/main/resources/base/users.txt");
    List<User> users = new ArrayList<>();
    Gson gson = new GsonBuilder().setPrettyPrinting().create();

    {
        if (!userFile.exists()) {
            try {
                userFile.createNewFile();
                users.add(User.builder().name("Murtazayev").userName(null).id(254632678).build());
                writeUser(users);
            } catch (IOException e) {
                e.printStackTrace();
            }
        }

    }

    public void writeUser(List<User> users) {
        try (Writer writer = new FileWriter(userFile)) {
            writer.write(gson.toJson(users));
        } catch (IOException e) {
            e.printStackTrace();
        }
    }


    @Override
    public String getBotToken() {
        return "5032407406:AAF5SWLY08Zhff0i2b3GubuZy2OvDt3Wilk";
    }

    @Override
    public void onUpdateReceived(Update update) {
        ReplyKeyboardSender keyboardSender = new ReplyKeyboardSender();

        if (update.hasMessage()) {

            SendMessage sendMessage = new SendMessage();
            if (update.getMessage().getText().equals("/start")) {
                sendMessage.setChatId(update.getMessage().getChatId());
                Message message = update.getMessage();

                sendMessage.setText("**Assalomu alaykum " + message.getFrom().getFirstName() + "\nBotimizga xush kelibsiz" +
                        "\nSizga qanday yordam bera olamiz?");

                users = getUsersList();
                boolean hasUser = false;
                for (User user1 : users) {
                    if (user1.getId().equals(message.getFrom().getId())) {
                        hasUser = true;
                        break;
                    }
                }
                if (!hasUser) {
                    User user = User.builder().name(message.getFrom().getFirstName())
                            .userName(message.getFrom().getUserName())
                            .id(message.getFrom().getId())
                            .chatId(String.valueOf(update.getMessage().getChatId()))
                            .build();
                    users.add(user);
                    writeUser(users);
                }

                sendMessage.setReplyMarkup(keyboardSender.createKeyboard(new String[]{"Korrupsiya haqida xabar berish", "Bog'lanish"}));
                try {
                    execute(sendMessage);
                } catch (TelegramApiException e) {

                }
            }
            else if (update.getMessage().getText().equals("Korrupsiya haqida xabar berish")) {
                sendMessage.setChatId(update.getMessage().getChatId());

                sendMessage.setText("Eslatib o'tamiz, siz haqingizdagi barcha ma'lumotlar sir saqlanadi. " +
                        "\nKorrupsiya yuz bergan viloyatni tanlang");
                users = getUsersList();
                for (User user : users) {
                    if (update.getMessage().getFrom().getId().equals(user.getId())) {
                        user.setStage(1);
                        break;
                    }
                }
                sendMessage.setReplyMarkup(keyboardSender.createKeyboard(new String[]
                        {
                                "Toshkent shahar",
                                "Toshkent viloyat",
                                "Sirdaeyo viloyati",
                                "Jizzax viloyati",
                                "Samarqand viloyati",
                                "Navoiy viloyati",
                                "Buxoro viloyati",
                                "Qashqadaryo viloyati",
                                "Surxondaryo viloyati",
                                "Xorazm viloyati",
                                "Farg'ona viloyati",
                                "Namangan viloyati",
                                "Qoraqalpog'iston Respublikasi"
                        }));

                try {
                    execute(sendMessage);
                } catch (TelegramApiException e) {

                }
                writeUser(users);
            }
            else if (update.getMessage().getText().equals("Bog'lanish")){
                sendMessage.setChatId(update.getMessage().getChatId());
                sendMessage.setText("Telefon:    +998712020402" + "\nCall center:    7777" +
                        "\nWeb sayt:     www.anticorruption.uz" + "\nPochta:   antikor@exat.uz");

                sendMessage.setReplyMarkup(keyboardSender.createKeyboard(new String[]{"Korrupsiya haqida xabar berish", "Bog'lanish"}));
                SendLocation location = new SendLocation();
                location.setChatId(update.getMessage().getChatId());
                location.setLatitude(41.295196f);
                location.setLongitude(69.266044f);
                try {
                    execute(sendMessage);
                }catch (Exception ignored){

                }
                try {
                    execute(location);
                } catch (TelegramApiException e) {

                }
            }
            else if (update.getMessage().getText().equals("Arizani yuborish")) {
                sendMessage.setChatId(update.getMessage().getChatId());

                for (User user : getUsersList()) {
                    if (update.getMessage().getFrom().getId().equals(user.getId())) {
                        Application app = user.getLastApplication();
                        sendMessage.setText("Arizangiz qabul qilindi, tez orada siz bilan bog'lanamiz" +
                                "\n\n Sizning arizangiz: \nViloyat:     " + app.getRegion() +
                                "\nTuman:     " + app.getDistrict() + "\nTashkilot nomi:     " + app.getOrganization() +
                                "\nBatafsil:     " + app.getMore() + "\nEmailingiz:     " + app.getEmail());
                    }
                }
                sendMessage.setReplyMarkup(keyboardSender.createKeyboard(new String[]{"Korrupsiya haqida xabar berish", "Bog'lanish"}));

                try {
                    execute(sendMessage);
                } catch (TelegramApiException e) {

                }
            } else {
                users = getUsersList();
                for (User user : users) {
                    if (update.getMessage().getFrom().getId().equals(user.getId())) {
                        if (user.getStage() == 1) {
                            Application application = Application.builder().region(update.getMessage().getText()).build();
                            sendMessage.setChatId(update.getMessage().getChatId());
                            sendMessage.setText("Iltimos tumanni tanlang: ");
                            sendMessage.setReplyMarkup(keyboardSender.createKeyboard(new String[]
                                    {
                                            "Sergeli tumani",
                                            "Yunusobod tumani",
                                            "Olmazor tumani",
                                            "Mirzo-Ulug'bek tumani",
                                            "Chilonzor tumani",
                                            "Yakkasaroy tumani",
                                            "Mirobod tumani",
                                            "Yashnobod tumani",
                                            "Bektemir tumani",
                                            "Uchtepa tumani",
                                            "Shayxontohur tumani",
                                    }));
                            try {
                                execute(sendMessage);
                            } catch (TelegramApiException e) {

                            }
                            user.getApplications().add(application);
                            user.setStage(2);
                            break;
                        }
                        if (user.getStage() == 2) {
                            user.getLastApplication().setDistrict(update.getMessage().getText());
                            sendMessage.setChatId(update.getMessage().getChatId());
                            sendMessage.setText("Korrupsiya ro'y bergan tashkilot nomini kiriting: ");
                            sendMessage.setReplyMarkup(null);
                            try {
                                execute(sendMessage);
                            } catch (TelegramApiException e) {

                            }
                            user.setStage(3);
                            break;
                        }
                        if (user.getStage() == 3) {
                            user.getLastApplication().setOrganization(update.getMessage().getText());
                            sendMessage.setChatId(update.getMessage().getChatId());
                            sendMessage.setText("Batafsil ma'lumotlarni kiriting: ");
                            try {
                                execute(sendMessage);
                            } catch (TelegramApiException e) {

                            }
                            user.setStage(4);
                            break;
                        }
                        if (user.getStage() == 4) {
                            user.getLastApplication().setMore(update.getMessage().getText());
                            sendMessage.setChatId(update.getMessage().getChatId());
                            sendMessage.setText("Siz bilan bog'lanishimiz uchun emailingizni kiriting: ");
                            try {
                                execute(sendMessage);
                            } catch (TelegramApiException e) {

                            }
                            user.setStage(5);
                            break;
                        }
                        if (user.getStage() == 5) {
                            user.getLastApplication().setEmail(update.getMessage().getText());
                            sendMessage.setChatId(update.getMessage().getChatId());
                            sendMessage.setText("Telefon raqamingizni kiriting: ");
                            try {
                                execute(sendMessage);
                            } catch (TelegramApiException e) {

                            }
                            user.setStage(6);
                            break;
                        }
                        if (user.getStage() == 6) {
                            user.getLastApplication().setTelephoneNumber(update.getMessage().getText());
                            sendMessage.setChatId(update.getMessage().getChatId());
                            sendMessage.setText("Qo'shimcha ma'lumot uchun fayl biriktiring(PDF, JPEG, MP4)");
                            sendMessage.setReplyMarkup(keyboardSender.createKeyboard(new String[]{"Arizani yuborish"}));
                            try {
                                execute(sendMessage);
                            } catch (TelegramApiException e) {

                            }
                            user.setStage(7);
                            break;
                        }
                        if (user.getStage() == 7) {
                            sendMessage.setChatId(update.getMessage().getChatId());

                            sendMessage.setText("Ma'lumot yuklandi, yana dalil bo'lsa yuklang va \"Arizani yuborish\" tugmasini bosing");

                            try {
                                execute(sendMessage);
                            } catch (TelegramApiException e) {

                            }
                            break;
                        }

                    }
                }
                writeUser(users);
            }
        }
    }

    public List<User> getUsersList() {
        GsonUserHelper userHelper = new GsonUserHelper();
        return userHelper.converter(userFile);
    }


    @Override
    public String getBotUsername() {
        return "fair_uzbekistan_bot";
    }
}
