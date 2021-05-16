import {
  IonContent,
  IonHeader,
  IonPage,
  IonTitle,
  IonToolbar,
} from "@ionic/react";
import classes from "./FoodTracker.module.scss";
import Select from "react-select";
import { useForm, Controller } from "react-hook-form";

const options = [
  { value: "39128382392", label: "Chocolate" },
  { value: "91283982309", label: "Strawberry" },
  { value: "69684395843", label: "Vanilla" },
];

type OptionType = {
  value: string;
  label: string;
} | null;

const FoodTracker: React.FC = () => {
  const {
    register,
    handleSubmit,
    control,
    formState: { errors },
  } = useForm();

  const onSubmit = (data: any) => {
    // TODO: send data to back-end
    console.log(data);
  };

  return (
    <IonPage className={classes.FoodTracker}>
      <IonHeader>
        <IonToolbar>
          <IonTitle>Food tracker</IonTitle>
        </IonToolbar>
      </IonHeader>
      <IonContent>
        <form onSubmit={handleSubmit(onSubmit)}>
          <Controller
            name="foodCode"
            control={control}
            render={({ field: { onChange, onBlur, value } }) => (
              <Select
                onBlur={onBlur}
                onChange={(option: OptionType) => {
                  return onChange(option?.value);
                }}
                value={options.find((option) => option.value === value)}
                options={options}
              />
            )}
          />
          <input
            type="number"
            step="0.01"
            placeholder={"Per 100g"}
            {...register("amount", { required: true })}
          />
          {errors.amount && <span>This field is required</span>}
          <input type="submit" value={"🥚 Record intake"} />
        </form>
      </IonContent>
    </IonPage>
  );
};

export default FoodTracker;
