package uz.fairUzbekistan.model;

import lombok.*;

import java.util.ArrayList;
import java.util.List;

@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class User {
    private String name;
    private String userName;
    private String chatId;
    private Integer id;
    private int stage = 1;
    private List<Application> applications = new ArrayList<>();

    public void updateStage() {
        this.stage++;
    }

    public Application getLastApplication(){
        return applications.get(applications.size()-1);
    }
}
