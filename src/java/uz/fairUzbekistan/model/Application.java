package uz.fairUzbekistan.model;

import lombok.*;

@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class Application {
    private String region;
    private String district;
    private String organization;
    private String more;
    private String email;
    private String telephoneNumber;
    private String state;
}
