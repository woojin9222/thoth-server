import { NestFactory } from '@nestjs/core';
import { AppModule } from './app.module';
import { UsersService } from './user/user.service';

async function bootstrap() {
  const app = await NestFactory.create(AppModule);

  const userService = app.get(UsersService);

  await app.listen(process.env.PORT ?? 3000);
}
bootstrap();
